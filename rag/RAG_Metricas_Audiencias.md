# RAG — Métricas y benchmarks de audiencias digitales

*Conocimiento de dominio para el enjambre · benchmarks con fuente · 04/06/2026*

> Todos los benchmarks llevan fuente y periodo. Son valores de referencia del sector, no
> objetivos: el contexto (industria, canal, madurez) manda. **Verificar siempre en vivo.**

---

## 1. Analítica web (GA4 / Search Console / GTM)

| KPI | Definición | Benchmark típico | Fuente |
|---|---|---|---|
| Engagement rate (GA4) | % de sesiones "engaged" (>10s, conversión o ≥2 páginas) | Media ~62%; rango 50–65% | Semrush / Arvo Digital (2024–25) |
| Bounce rate | 100% − engagement rate (GA4) | Mediana ~45%; <40% excelente, >70% revisar | Databox GA4 (ago-23) / Contentsquare 2024 |
| Duración media de sesión | Tiempo total / nº sesiones | Mediana ~2 m 38 s (todas industrias) | Databox — GA4 Industry Benchmarks |
| Tasa de conversión web | (Conversiones / sesiones) × 100 | 1–4% general; eCommerce ~2,2%; paid search ~2,55% | First Page Sage / Contentsquare 2024 |
| Scroll rate | % sesiones con scroll significativo (≥90%) | ~50% (y descendiendo) | Contentsquare 2024 |

**Conversión por industria (B2C):** Hoteles 3,6% · Healthcare 3,1% · Entretenimiento 2,9% ·
Food&Bev 2,6% · Apparel 2,3% · eCommerce 2,2% · Finanzas 1,7% · Lujo 1,4% · SaaS 1,2%.
**(B2B):** Legal 7,4% · HVAC 3,1% · Staffing 2,9% · Real Estate 2,8% · Manufacturing 2,1% ·
Financial Services 1,9% · SaaS B2B 1,1%. *(First Page Sage, ene–sep 2023.)*

## 2. Retención

| Métrica | Benchmark | Fuente |
|---|---|---|
| Retención web D30 por sector | IT/software ~40% · seguros ~35% · media/serv. prof. ~30% · retail ~20% · viajes ~15% | Contentsquare / Growth-onomics |
| Retención app D1 / D30 | D1 ~25–30% (excelente >35%) · D30 ~5–6% global | Pushwoosh Benchmarks 2025 |

## 3. SEO (Search Console / Semrush / Ahrefs)

- **CTR orgánico por posición:** muy concentrado en el top-3; cae fuerte a partir de la posición 4–5. Verificar con datos propios de Search Console.
- Métricas clave: impresiones, clics, CTR, posición media, keywords posicionadas, autoridad.

## 4. Redes y email

- **Redes:** alcance, impresiones, engagement rate por plataforma (varía mucho; el engagement medio orgánico tiende a ser bajo, <1–3% en las grandes plataformas).
- **Email / newsletter:** open rate y CTR varían por sector; usar benchmarks del proveedor (Mailchimp publica medias por industria). Open rate medio suele situarse ~20% según sector.

## 5. Plan de medición (estructura canónica)

1. **Objetivos de negocio** → 2. **Estrategias/tácticas** → 3. **KPIs** (SMART, traducen el objetivo) → 4. **Métricas de soporte** → 5. **Segmentos/dimensiones** → 6. **Targets**.
**Regla de foco:** 5–7 KPIs bien elegidos por etapa, no volumen.
*(Fuentes: Fresh Egg, Smart Insights, Avinash Kaushik.)*

## 6. Guía de etiquetado (event tracking plan)

Documento vivo (hoja de cálculo) con eventos + parámetros. Empezar con 3–5 eventos de negocio.
**Naming GA4:** snake_case, minúsculas, empezar por letra, sin espacios; patrón verbo o
sujeto_verbo (`page_view`, `file_download`). No usar prefijos reservados `ga_`, `firebase_`,
`google_`. Reutilizar el mismo nombre de parámetro entre eventos. Documentar y versionar.
*(Fuentes: Analytics Mania, MeasureSchool, Google.)*

## 7. Calibración para datos sintéticos (demo)

Conversión 1–4% (eCommerce ~2,2%, paid search ~2,55%); engagement rate GA4 50–65% (media 62%);
bounce 44–49%; duración sesión ~2 m 30 s; retención web D30 por sector 15–40%.

## 8. Privacidad (regla operativa)

- **Público y agregado** (Trends, benchmarks, conversación pública en volumen) → uso libre, sin RGPD.
- **Personal** (GA4 con user_id, cookies, IP, CRM, listas de email) → RGPD/ePrivacy: consentimiento, anonimización, minimización. El analista debe saber **dónde está la línea**.

---

*RAG Métricas Audiencias v1.0 · 04/06/2026 · benchmarks con fuente, verificar en vivo*
