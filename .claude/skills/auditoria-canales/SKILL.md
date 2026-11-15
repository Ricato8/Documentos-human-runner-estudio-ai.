---
name: auditoria-canales
description: Audita el website humanrunner.co y/o el Instagram @humanrunner.co de Human Runner, buscando fricciones de compra, coherencia de marca y oportunidades de conversión. Úsala para el diagnóstico inicial o cuando pidan revisar la web, la tienda, el checkout o el perfil de Instagram.
---

# Auditoría de canales

1. Lee `CLAUDE.md`, `00_base-conocimiento/guia-de-voz.md` y `plantillas/auditoria-ux.md`.
2. **Website:** navega https://www.humanrunner.co. Si el acceso de red lo permite, usa Playwright con Chromium preinstalado y captura en móvil y desktop. Recorre home → colección → producto → carrito → inicio de checkout (sin comprar). Revisa claims, guía de tallas, envíos, cambios, medios de pago, velocidad y tracking visible (GA4, píxel).
3. **Instagram:** analiza https://www.instagram.com/humanrunner.co/ con la información pública disponible. Si no hay acceso, pide capturas o exportes de Insights.
4. Registra cada hallazgo con evidencia y severidad, y prioriza el top 5 por impacto/esfuerzo.
5. Guarda la auditoría web en `04_growth/auditorias/AAAA-MM-DD_auditoria-website.md` y la de IG en `02_content/reportes/AAAA-MM-DD_auditoria-instagram.md`. Las capturas van junto al informe en una subcarpeta `capturas/`.
6. Marca la tarea en `06_plan/plan-30-dias.md`.
