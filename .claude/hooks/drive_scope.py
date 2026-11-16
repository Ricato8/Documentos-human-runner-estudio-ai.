#!/usr/bin/env python3
"""Restringe el acceso a Google Drive a la carpeta autorizada de Human Runner.

Uso (desde .claude/settings.json):
  drive_scope.py pre   -> PreToolUse: bloquea (exit 2) lo que salga de la carpeta.
  drive_scope.py post  -> PostToolUse: registra los IDs devueltos al listar la carpeta.

Reglas:
  - Búsquedas: solo `parentId = '<carpeta autorizada o subcarpeta conocida>'`, combinadas
    únicamente con `and` (sin `or` / `not`, que permitirían salir del alcance).
  - Lecturas por ID: solo IDs encontrados dentro de la carpeta (semilla + descubiertos).
  - Escrituras en Drive (crear, editar, copiar, compartir, borrar): bloqueadas.
  - Listados globales (recientes, unidades compartidas): bloqueados.
  - WebFetch a docs.google.com / drive.google.com: bloqueado (usar las herramientas de Drive).
"""
import json, os, re, sys

BASE = os.path.join(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()), ".claude", "drive-scope")
SEED = os.path.join(BASE, "allowlist-semilla.txt")
LOCAL = os.path.join(BASE, "allowlist.local.txt")
CFG = os.path.join(BASE, "config.json")

READ_BY_ID = {"read_file_content", "get_file_metadata", "download_file_content",
              "list_file_revisions", "get_file_permissions"}
SEARCH = {"search_files"}

def load_ids():
    ids = set()
    for p in (SEED, LOCAL):
        try:
            with open(p, encoding="utf-8") as f:
                ids.update(l.strip() for l in f if l.strip() and not l.startswith("#"))
        except FileNotFoundError:
            pass
    try:
        ids.add(json.load(open(CFG, encoding="utf-8"))["carpeta_raiz_id"])
    except Exception:
        pass
    return ids

def deny(msg):
    sys.stderr.write("BLOQUEADO por la política de acceso a Drive de Human Runner: " + msg +
                     " Solo está autorizada la carpeta https://drive.google.com/drive/folders/"
                     "1LeKiRQ9hujnP9DAhWLc-D5QEKHR8-NTN y sus subcarpetas, en modo lectura.\n")
    sys.exit(2)

def strip_quoted(q):
    return re.sub(r"'(?:\\.|[^'\\])*'", "''", q)

def check_query(q, allowed):
    bare = strip_quoted(q)
    if re.search(r"\b(or|not)\b", bare, re.I):
        deny("la búsqueda usa 'or' o 'not', que podrían salir de la carpeta. Usa solo 'and'.")
    parents = re.findall(r"parentId\s*=\s*'([^']+)'", q)
    if not parents:
        deny("toda búsqueda debe incluir parentId = '<carpeta autorizada>'.")
    bad = [p for p in parents if p not in allowed]
    if bad:
        deny(f"la carpeta {bad[0]} no está dentro del alcance autorizado.")

def pre(data):
    tool = data.get("tool_name", "")
    ti = data.get("tool_input", {}) or {}
    if tool in ("WebFetch", "Fetch") or tool.endswith("__fetch"):
        url = str(ti.get("url", ""))
        if re.search(r"(docs|drive)\.google\.com", url):
            deny("no se leen archivos de Google por URL; usa las herramientas de Drive dentro de la carpeta.")
        return
    if not tool.startswith("mcp__Google_Drive__"):
        return
    action = tool.split("__")[-1]
    allowed = load_ids()
    if action in SEARCH:
        check_query(str(ti.get("query", "")), allowed)
    elif action in READ_BY_ID:
        fid = str(ti.get("fileId", ""))
        if fid not in allowed:
            deny(f"el archivo {fid or '(sin ID)'} no se ha encontrado dentro de la carpeta autorizada. "
                 "Lista primero la carpeta con search_files y parentId.")
    else:
        deny(f"la herramienta '{action}' no está permitida (acceso de solo lectura, limitado a la carpeta).")

def post(data):
    tool = data.get("tool_name", "")
    if not tool.endswith("__search_files"):
        return
    blob = json.dumps(data.get("tool_response", ""), ensure_ascii=False)
    found = set(re.findall(r'\\*"id\\*"\s*:\s*\\*"([A-Za-z0-9_-]{10,})', blob))
    new = found - load_ids()
    if new:
        os.makedirs(BASE, exist_ok=True)
        with open(LOCAL, "a", encoding="utf-8") as f:
            f.writelines(i + "\n" for i in sorted(new))

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "pre"
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    (post if mode == "post" else pre)(data)
    sys.exit(0)
