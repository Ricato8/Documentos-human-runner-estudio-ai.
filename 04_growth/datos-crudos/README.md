# Datos crudos — exportes de las plataformas

> El estudio **no tiene acceso directo** a Instagram Insights, GA4 ni a la tienda. Los datos de tráfico de HR no son públicos.
> Sube aquí los exportes y el agente `growth` (o la skill `reporte-semanal`) construye la línea base y el dashboard.
> Nombre de archivo: `AAAA-MM-DD_a_AAAA-MM-DD_<fuente>.csv`

Pide siempre **dos periodos**: los últimos 90 días y los 90 días anteriores, para poder comparar.

## 1. Instagram (`instagram/`)
Requiere cuenta profesional (creador o empresa).

**Opción A, Meta Business Suite (recomendada, exporta CSV):**
1. Abre business.facebook.com → **Insights** (o *Estadísticas*).
2. En **Resultados** y **Contenido**, elige el rango de fechas.
3. Haz clic en **Exportar datos** → CSV.

**Opción B, app de Instagram:** Perfil → **Panel profesional** → **Estadísticas** → *Últimos 90 días*. Toma capturas de *Cuentas alcanzadas*, *Interacción*, *Seguidores* y *Actividad del perfil* (visitas y **toques en enlace externo**).

Métricas mínimas: alcance, impresiones, visitas al perfil, **toques en el enlace de la bio**, seguidores (ganados y perdidos), interacciones, guardados y compartidos por publicación, y audiencia (ciudades, edades, género).

## 2. Website — Google Analytics 4 (`ga4/`)
1. analytics.google.com → propiedad de humanrunner.co.
2. **Informes → Adquisición → Adquisición de tráfico** → rango de fechas → Compartir → **Descargar CSV**.
3. Repite con **Interacción → Páginas y pantallas**, **Monetización → Compras de comercio electrónico** y **Usuario → Atributos demográficos / Tecnología**.
4. Filtro clave: sesiones con fuente `instagram` o `l.instagram.com` (tráfico de Instagram a la web).

Si no hay GA4 instalado, revisa las estadísticas de la plataforma de la tienda (punto 3) y anótalo: instalarlo será la primera tarea de Growth.

## 3. Ecommerce (`ecommerce/`)
- **Shopify:** Análisis → Informes → *Sesiones por fuente de referencia*, *Ventas por producto*, *Embudo de conversión online* → Exportar.
- **WooCommerce:** WooCommerce → Análisis → Pedidos / Productos → Descargar.
- Otra plataforma: exporta pedidos (fecha, valor, productos, ciudad, cliente nuevo o recurrente) y sesiones por fuente.

## Alternativa: dar acceso de lectura
- GA4: Administrar → Gestión de acceso → rol **Lector**.
- Meta Business Suite: Configuración → Personas → acceso parcial a Insights.
- Ecommerce: usuario con permisos solo de lectura de informes.

**Privacidad:** antes de subir exportes de pedidos, elimina nombres, correos, teléfonos y direcciones de los clientes. Basta con la ciudad.
