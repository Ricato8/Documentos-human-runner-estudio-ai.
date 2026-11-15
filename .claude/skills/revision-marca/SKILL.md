---
name: revision-marca
description: Revisa un texto (copy, guion, ficha de producto, anuncio, email o mensaje) contra la voz y la regla de claims de Human Runner y devuelve el veredicto con la versión corregida. Úsala cuando pidan revisar tono, claims o "¿esto está on-brand?".
---

# Revisión de marca

Delega en el agente `brand-guardian` pasándole el texto completo y su contexto (pieza, colección, objetivo). Si el agente no está disponible, aplica tú directamente `00_base-conocimiento/guia-de-voz.md`:

1. Busca palabras de alerta y especificaciones sin verificar en `producto/catalogo.md`.
2. Evalúa los 6 rasgos de personalidad y la inclusión de todos los niveles de corredor.
3. Verifica que no haya testimonios, cifras o alianzas inventadas.
4. Devuelve: **veredicto**, una tabla *fragmento → problema → sugerencia* y la **versión corregida**.
