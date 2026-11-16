# Sistema de llamado de agentes — Estudio Digital AI · Human Runner

| | |
|---|---|
| **Objetivo** | Definir cómo se llama a cada agente del estudio, para qué actividad y qué entrega, de modo que cualquier persona del equipo HR pueda pedir trabajo sin ambigüedad |
| **Fecha** | 2026-11-15 · v1.0 |
| **Fuentes** | `briefing-maestro.md` §11 y §13 · `.claude/agents/` · `.claude/skills/` |
| **Alcance** | 6 agentes · 6 skills · 46 actividades |

---

## 1. Cómo funciona el llamado

En Claude Code el trabajo se pide en lenguaje natural dentro de una sesión abierta en la carpeta del repositorio. Hay tres formas de activar a un agente:

| Forma | Cómo se escribe | Cuándo usarla |
|---|---|---|
| **A. Llamado explícito al agente** | `Usa el agente research para …` | Cuando sabes qué frente debe hacerlo. **Es la forma recomendada.** |
| **B. Skill (comando)** | `/parrilla-contenido diciembre 2026` | Tareas recurrentes con un procedimiento fijo |
| **C. Delegación automática** | Pides la tarea sin nombrar un agente: `Investiga las marcas de trail en Medellín` | Claude elige el agente según su descripción. Rápido, pero menos predecible |

**Qué pasa al llamar a un agente:**
1. El agente arranca con contexto limpio y lee `CLAUDE.md` y los archivos de su frente.
2. Ejecuta la tarea solo con sus herramientas: los agentes de investigación tienen búsqueda web y `brand-guardian` solo puede leer.
3. Guarda el entregable en su carpeta usando la plantilla correspondiente.
4. Devuelve un resumen a la conversación principal.

### Formato estándar de llamado
Usa esta estructura para pedidos importantes. Para tareas simples basta una línea.

```
Usa el agente <nombre> para <actividad>.
Objetivo de negocio: <qué decisión o resultado busca>
Alcance: <ciudad / colección / segmento / periodo>
Insumos: <archivos adjuntos o rutas en el repo>
Entregable: <formato esperado>  ·  Plazo/periodo: <...>
```

### Reglas que aplican a todos los llamados
- **Drive:** los agentes solo leen la carpeta HR (https://drive.google.com/drive/folders/1LeKiRQ9hujnP9DAhWLc-D5QEKHR8-NTN) y sus subcarpetas. Un hook bloquea todo lo demás.
- **Datos:** si el pedido requiere cifras de HR (ventas, tráfico, Insights) y no están en el repo, el agente las pide. **No las inventa.**
- **Aprobación humana:** pauta, precios, descuentos, alianzas, producción y cualquier contacto con terceros.
- **Nada sale del repositorio:** los agentes no publican en Instagram, no envían correos y no contactan a nadie.
- **Revisión de marca:** todo texto que verá un cliente o aliado pasa por `brand-guardian` antes de entregarse.
- **Cierre de ciclo:** las decisiones van a `07_decisiones-y-aprendizajes/`.

---

## 2. Mapa general

| # | Agente | Frente | Llamado base | Skills asociadas | Frecuencia | Carpeta de salida |
|---|---|---|---|---|---|---|
| 1 | `research` | A. Research & Market Intelligence | `Usa el agente research para …` | `/benchmark-competidor` | Semanal / mensual | `01_research/` |
| 2 | `content` | B. Content & Social Media | `Usa el agente content para …` | `/parrilla-contenido` | Semanal | `02_content/` |
| 3 | `hunting` | C. Hunting & Business Opportunities | `Usa el agente hunting para …` | `/ficha-oportunidad` | Semanal | `03_hunting/` |
| 4 | `growth` | D. Growth & Performance | `Usa el agente growth para …` | `/reporte-semanal` · `/auditoria-canales` | Semanal | `04_growth/` |
| 5 | `product-intelligence` | E. Product Intelligence | `Usa el agente product-intelligence para …` | — | Mensual | `05_product-intelligence/` |
| 6 | `brand-guardian` | Control de marca (transversal) | `Usa el agente brand-guardian para revisar …` | `/revision-marca` | Antes de cada entrega | Responde en la conversación |

---

## 3. Fichas por agente

### 3.1 `research` — Research & Market Intelligence

**Rol:** investigar el mercado, los usuarios, las tendencias y la competencia.
**Herramientas:** lectura y escritura en el repo, búsqueda web y lectura de páginas.
**Llámalo cuando** necesites contexto externo para tomar una decisión: quién compite, a qué precio, qué tendencias hay, quién es el cliente.

| # | Actividad | Llamado de ejemplo | Entregable → ubicación |
|---|---|---|---|
| R1 | Mercado de running y trail en Colombia | `Usa el agente research para hacer un informe del mercado de running y trail en Colombia: tamaño, crecimiento y carreras principales` | Informe → `01_research/informes/` |
| R2 | Competidores directos e indirectos | `Usa el agente research para identificar competidores directos e indirectos de HR en Colombia y clasificarlos` | `benchmark/competidores.csv` + informe |
| R3 | Benchmark de una marca | `/benchmark-competidor <marca>` | Ficha → `01_research/benchmark/` |
| R4 | Precios y posicionamiento | `Usa el agente research para comparar rangos de precio de camisetas técnicas de running en Colombia` | Informe con tabla de precios |
| R5 | Tendencias de materiales y diseño | `Usa el agente research para un reporte de tendencias de materiales y gráfica en ropa de running 2026-2027` | `01_research/tendencias/` |
| R6 | Eventos y comunidades | `Usa el agente research para analizar el ecosistema de carreras y comunidades running en Antioquia` | Informe (luego se pasa a `hunting`) |
| R7 | Perfiles de usuario y validación de segmentos | `Usa el agente research para diseñar la encuesta y la guía de entrevistas que validen los 4 segmentos` | `01_research/audiencias/` |
| R8 | Necesidades no resueltas y mapa de oportunidades | `Usa el agente research para construir un mapa de oportunidades para HR a partir de los informes existentes` | Informe con matriz impacto/esfuerzo |

**Insumos útiles:** competidores que HR ya tenga en mente; resultados de encuestas o entrevistas.
**No hace:** cifras de ventas o tráfico de HR (eso es `growth`), ni contactos (eso es `hunting`).

---

### 3.2 `content` — Content & Social Media Intelligence

**Rol:** planificar, producir y optimizar la comunicación digital.
**Herramientas:** lectura y escritura en el repo, búsqueda web y lectura de páginas.
**Llámalo cuando** necesites qué decir, cómo, cuándo y en qué formato.

| # | Actividad | Llamado de ejemplo | Entregable → ubicación |
|---|---|---|---|
| C1 | Estrategia editorial | `Usa el agente content para proponer la estrategia editorial del Q1 2027 con los 6 pilares` | `02_content/estrategia/` |
| C2 | Calendario y parrilla | `/parrilla-contenido diciembre 2026, objetivo: tráfico a la web de Majors` | CSV → `02_content/calendarios/` |
| C3 | Conceptos creativos | `Usa el agente content para proponer 3 conceptos creativos para Huru alrededor de "No eres perfecto. Eres constante."` | `02_content/estrategia/` |
| C4 | Copies y descripciones de producto | `Usa el agente content para escribir la descripción web de <referencia> con los claims del catálogo` | `02_content/copies/` |
| C5 | Campaña de lanzamiento | `Usa el agente content para armar el brief de campaña del lanzamiento de <colección>` | `02_content/campanas/` |
| C6 | Guiones de Reels | `Usa el agente content para escribir 4 guiones de Reels del pilar Educación sobre ventilación y secado` | `02_content/guiones/` |
| C7 | Contenido de la competencia y tendencias | `Usa el agente content para analizar qué formatos publican las marcas de competidores.csv` | `02_content/reportes/` |
| C8 | Dinámicas de comunidad | `Usa el agente content para proponer 5 formatos de comunidad con corredores reales` | `02_content/estrategia/` |
| C9 | Desempeño de publicaciones | `Usa el agente content para analizar el rendimiento de los posts del último mes` (adjuntar el exporte de Insights) | `02_content/reportes/` |

**Insumos útiles:** catálogo con claims verificados, exportes de Insights y fotos o videos disponibles.
**No hace:** publicar. Entrega borradores, y todo texto pasa por `brand-guardian`.

---

### 3.3 `hunting` — Hunting & Business Opportunities

**Rol:** identificar, organizar y priorizar oportunidades comerciales y alianzas.
**Herramientas:** lectura y escritura en el repo, búsqueda web y lectura de páginas.
**Llámalo cuando** necesites con quién conectar: clubes, carreras, tiendas, aliados o creadores.

| # | Actividad | Llamado de ejemplo | Entregable → ubicación |
|---|---|---|---|
| H1 | Clubes y grupos de running | `Usa el agente hunting para mapear clubes de running de Medellín y el Valle de Aburrá` | Filas en `prospectos.csv` |
| H2 | Entrenadores y comunidades | `Usa el agente hunting para identificar entrenadores con comunidad activa en Antioquia` | `prospectos.csv` |
| H3 | Organizadores y calendario de carreras | `Usa el agente hunting para construir el calendario de carreras de ruta y trail en Colombia de 2027` | `eventos.csv` |
| H4 | Tiendas y distribuidores | `Usa el agente hunting para identificar tiendas especializadas en running en Medellín y Bogotá` | `prospectos.csv` |
| H5 | Marcas para colaboraciones | `Usa el agente hunting para proponer 10 marcas compatibles para una colaboración con HR` | `prospectos.csv` + fichas |
| H6 | Atletas y creadores | `Usa el agente hunting para identificar creadores de contenido de running y trail afines al tono de HR` | `prospectos.csv` |
| H7 | Oportunidades de activación | `Usa el agente hunting para detectar carreras de 2027 con oportunidad de activación de marca` | `eventos.csv` + fichas |
| H8 | Ficha y priorización de una oportunidad | `/ficha-oportunidad <nombre del club o evento>` | `03_hunting/fichas/` |
| H9 | Revisión del pipeline | `Usa el agente hunting para revisar el estado del pipeline y proponer los próximos pasos de la semana` | Resumen + CSV actualizado |

**Insumos útiles:** aliados y clubes que HR ya conozca, y eventos donde ya participó.
**No hace:** contactar. Redacta borradores; una persona aprueba y envía. Solo usa datos públicos y profesionales (Ley 1581).

---

### 3.4 `growth` — Growth & Performance

**Rol:** analizar los canales y mejorar la adquisición, la conversión y la retención.
**Herramientas:** lectura y escritura en el repo, terminal (scripts de análisis y navegador para auditorías) y lectura de páginas.
**Llámalo cuando** necesites saber qué está funcionando, dónde se pierde la venta y qué optimizar.

| # | Actividad | Llamado de ejemplo | Entregable → ubicación |
|---|---|---|---|
| G1 | Reporte semanal | `/reporte-semanal` (con los exportes en `04_growth/datos-crudos/`) | `04_growth/reportes/` + dashboard |
| G2 | Línea base y dashboard | `Usa el agente growth para construir la línea base de KPIs con los exportes de datos-crudos` | `04_growth/dashboard.md` |
| G3 | Embudo y abandono de carrito | `Usa el agente growth para analizar el embudo de conversión y el abandono de carrito de los últimos 90 días` | `04_growth/reportes/` |
| G4 | Auditoría UX/CRO del website | `/auditoria-canales website` | `04_growth/auditorias/` |
| G5 | Auditoría de Instagram | `/auditoria-canales instagram` | `02_content/reportes/` |
| G6 | Medición de campañas | `Usa el agente growth para medir la campaña <utm_campaign>` | `04_growth/campanas/` |
| G7 | Productos de mayor interés | `Usa el agente growth para identificar las referencias más vistas y más vendidas por colección` | Informe |
| G8 | Rendimiento de promociones | `Usa el agente growth para evaluar el resultado de la promoción <nombre>` | `04_growth/campanas/` |
| G9 | Acciones de adquisición y recompra | `Usa el agente growth para proponer 3 acciones de recompra con hipótesis y métrica` | Informe + `hipotesis.md` |
| G10 | UTMs | `Usa el agente growth para generar los links UTM de la parrilla de diciembre` | Parrilla actualizada |

**Insumos obligatorios:** exportes de GA4, de la tienda y de Instagram en `04_growth/datos-crudos/`. Sin ellos, solo puede auditar y proponer, no medir.
**No hace:** aprobar pauta, presupuestos ni descuentos. Los propone para decisión humana.

---

### 3.5 `product-intelligence` — Product Intelligence

**Rol:** aportar evidencia para la evolución del portafolio.
**Herramientas:** lectura y escritura en el repo, búsqueda web y lectura de páginas.
**Llámalo cuando** se vaya a decidir qué producir, mejorar o lanzar.

| # | Actividad | Llamado de ejemplo | Entregable → ubicación |
|---|---|---|---|
| P1 | Benchmark de prendas | `Usa el agente product-intelligence para comparar 10 camisetas técnicas de running de la competencia` | `matriz-atributos.csv` + informe |
| P2 | Materiales y tecnologías | `Usa el agente product-intelligence para investigar telas técnicas de proveedores colombianos frente a la referencia Vértigo` | `benchmark-producto/` |
| P3 | Feedback de clientes | `Usa el agente product-intelligence para clasificar los comentarios y DMs del último mes` (adjuntar) | `feedback/feedback.csv` + reporte |
| P4 | Aceptación de colecciones | `Usa el agente product-intelligence para evaluar la aceptación de Huru frente a Majors` (requiere datos de `growth`) | Informe |
| P5 | Nuevas referencias | `Usa el agente product-intelligence para proponer 3 ideas de nuevas referencias para trail` | `ideas-referencias/` |
| P6 | Tendencias de diseño | `Usa el agente product-intelligence para un reporte de tendencias gráficas para Majors 2027` | `benchmark-producto/` |
| P7 | Ediciones limitadas | `Usa el agente product-intelligence para identificar oportunidades de ediciones limitadas en el calendario 2027` | `ideas-referencias/` |

**Insumos útiles:** catálogo, fichas técnicas, devoluciones con su motivo y comentarios de clientes.
**No hace:** decidir producción ni costos; propone con evidencia. Tampoco asume especificaciones sin verificar.

---

### 3.6 `brand-guardian` — Control de marca

**Rol:** revisar tono, claims y veracidad. **Solo lee; no crea ni modifica archivos.**
**Llámalo** siempre antes de entregar cualquier texto externo: copies, guiones, fichas, anuncios, emails o mensajes a aliados.

| # | Actividad | Llamado de ejemplo | Respuesta |
|---|---|---|---|
| B1 | Revisión de un texto | `/revision-marca` + texto pegado | Veredicto + tabla de observaciones + versión corregida |
| B2 | Revisión de un archivo | `Usa el agente brand-guardian para revisar 02_content/calendarios/2026-12_parrilla.csv` | Igual, por cada pieza |
| B3 | Revisión de claims de producto | `Usa el agente brand-guardian para revisar los claims de la ficha de <referencia>` | Lista de claims aprobados y rechazados |

**Veredictos posibles:** Aprobado · Aprobado con cambios · Rechazado.

---

## 4. Flujos encadenados (varios agentes)

Para tareas grandes, pide el flujo completo en un solo mensaje: `Ejecuta el flujo <nombre>`. Claude llama a los agentes en orden y cada uno usa lo que dejó el anterior.

| Flujo | Secuencia | Cuándo |
|---|---|---|
| **Diagnóstico inicial (30 días)** | `growth` (G4, G5) → `research` (R2, R3) → `hunting` (H1, H3) → `content` (C1) → `growth` (G2) | Semanas 1 a 4 del plan |
| **Lanzamiento de colección** | `product-intelligence` (P1) → `research` (R4) → `content` (C5, C6, C2) → `brand-guardian` (B2) → `growth` (G10) → [lanzamiento] → `growth` (G6) | Cada lanzamiento |
| **Ciclo semanal** | `growth` (G1) → `content` (C9 → C2) → `brand-guardian` (B2) → `hunting` (H9) | Todas las semanas |
| **Alianza con club o evento** | `hunting` (H8) → `brand-guardian` (B1, sobre el borrador) → **aprobación humana** → seguimiento en el CSV | Por oportunidad A |
| **Nueva referencia** | `product-intelligence` (P3, P5) → `research` (R4, R5) → **decisión de HR** → `content` (C4) → `brand-guardian` (B3) | Por idea de producto |

Ejemplo de llamado encadenado:
```
Ejecuta el flujo de lanzamiento para la colección Majors "Ciudades" de febrero 2027.
Objetivo: 40 % de las ventas del mes desde tráfico de Instagram.
Insumos: fichas en 00_base-conocimiento/producto/catalogo.md
```

---

## 5. Agenda semanal de llamados

| Día | Llamado | Agente / skill | Responsable humano |
|---|---|---|---|
| Lunes | `/reporte-semanal` | `growth` | Revisa y define 1 acción |
| Martes | `/parrilla-contenido <semana siguiente>` → revisión de marca | `content` → `brand-guardian` | Aprueba piezas y producción |
| Miércoles | `Usa el agente hunting para revisar el pipeline` | `hunting` | Aprueba contactos |
| Jueves | `Usa el agente research para el monitoreo semanal de competencia y tendencias` | `research` | Lee hallazgos |
| Viernes | `Registra decisiones y aprendizajes de la semana` | Sesión principal | Valida |
| Mensual (1.ª semana) | Informe de mercado + Product Intelligence | `research` · `product-intelligence` | Decide portafolio y foco |

---

## 6. Matriz rápida: ¿a quién llamo?

| Necesito… | Agente |
|---|---|
| Saber qué hace la competencia o cuánto cobra | `research` |
| Posts, Reels, copies o un calendario | `content` |
| Clubes, carreras, tiendas o aliados | `hunting` |
| Cifras, conversión, campañas o mejoras de la web | `growth` |
| Ideas de producto, telas o feedback de clientes | `product-intelligence` |
| Saber si un texto está bien para publicar | `brand-guardian` |

---

## 7. Próximos pasos / decisión requerida
- [ ] Validar con HR quién es el **responsable humano** de cada frente (aprobaciones).
- [ ] Confirmar si se mantiene `brand-guardian` como sexto agente.
- [ ] Subir los primeros exportes a `04_growth/datos-crudos/` para activar `growth` (G1 y G2).
