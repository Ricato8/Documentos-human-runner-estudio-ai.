# Sistema de métricas — Human Runner

> Fuente: briefing §7.1 y §12. **Regla:** no confundir actividad con resultados. Compara siempre contra el periodo anterior.

## KPIs prioritarios de negocio (north stars)
| # | KPI | Fórmula | Fuente | Frecuencia | Línea base |
|---|---|---|---|---|---|
| 1 | Tráfico cualificado al website | Sesiones con engagement (GA4) de fuentes objetivo | GA4 | Semanal | _pendiente_ |
| 2 | Tasa de conversión | Compras / sesiones | GA4 + ecommerce | Semanal | _pendiente_ |
| 3 | Ventas por colección | Ingresos Huru / Majors / otras | Plataforma ecommerce | Semanal | _pendiente_ |
| 4 | CAC | Inversión en adquisición / clientes nuevos | Meta Ads + ecommerce | Mensual | _pendiente_ |
| 5 | AOV (ticket promedio) | Ingresos / pedidos | Ecommerce | Semanal | _pendiente_ |
| 6 | Tasa de recompra | Clientes con ≥2 pedidos / total de clientes | Ecommerce / CRM | Mensual | _pendiente_ |
| 7 | Clientes nuevos y recurrentes | % de pedidos de clientes nuevos | Ecommerce | Mensual | _pendiente_ |
| 8 | Conversión IG → web | Compras con utm_source=instagram / sesiones IG | GA4 (UTM) | Semanal | _pendiente_ |

## Indicadores por área
| Área | Indicadores | Fuente |
|---|---|---|
| Marca | Alcance, reconocimiento, menciones, búsquedas de marca | Google Search Console, Google Trends, IG |
| Instagram | Seguidores (neto), alcance, interacciones, **guardados y compartidos** | Instagram Insights |
| Comunidad | Respuestas, DMs, conversaciones, UGC, menciones | IG |
| Website | Sesiones, usuarios, fuentes de tráfico, páginas vistas, dispositivos, ubicación | GA4 |
| Conversión | View item → add to cart → begin checkout → purchase; abandono de carrito | GA4 / ecommerce |
| Comercial | Ventas, ticket promedio, ingresos por colección | Ecommerce |
| Producto | Referencias más consultadas, más vendidas, devoluciones (motivo) | GA4 + ecommerce |
| Hunting | Prospectos identificados, contactados, en conversación, alianzas cerradas | `03_hunting/prospectos.csv` |
| Retención | Clientes recurrentes, frecuencia y tiempo entre compras | Ecommerce / CRM |

## Embudo de referencia
```
Alcance IG → Visita al perfil → Clic al link (UTM) → Sesión web → Vista de producto
→ Add to cart → Inicio de checkout → Compra → Recompra
```
Cada reporte de Growth debe ubicar dónde está la mayor fuga del embudo.

## Accesos requeridos (pendiente de confirmar)
- [ ] Plataforma de ecommerce (¿Shopify / WooCommerce / otra?)
- [ ] Google Analytics 4
- [ ] Google Search Console
- [ ] Meta Business Suite / Instagram Insights
- [ ] Meta Ads Manager (si hay pauta)
- [ ] Exportes históricos de ventas
