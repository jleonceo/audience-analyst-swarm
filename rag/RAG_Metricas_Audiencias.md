# RAG: Métricas y benchmarks de audiencias digitales

*Conocimiento de dominio para el enjambre · benchmarks con fuente · 04/06/2026*

> Todos los benchmarks llevan fuente y periodo. Son valores de referencia del sector, no
> objetivos: el contexto (industria, canal, madurez) manda. **Verificar siempre en vivo.**

---

## 1. Analítica web (GA4 / Search Console / GTM)

| KPI | Definición | Benchmark típico | Fuente |
|---|---|---|---|
| Engagement rate (GA4) | % de sesiones "engaged" (>10s, conversión o ≥2 páginas) | Media ~62%; rango 50–65% | Semrush / Arvo Digital (2024–25) |
| Bounce rate | 100% − engagement rate (GA4) | Mediana ~45%; <40% excelente, >70% revisar | Databox GA4 (ago-23) / Contentsquare 2024 |
| Duración media de sesión | Tiempo total / nº sesiones | Mediana ~2 m 38 s (todas industrias) | Databox, GA4 Industry Benchmarks |
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

## 9. Benchmarks por canal de tráfico

Valores de referencia para comparar KPIs por canal. Las diferencias entre B2B y e-commerce son significativas.
Un canal por encima del rango de bounce es alerta; por debajo del rango de conversión merece revisión.

| Canal | Bounce rate típico | Duración media | Tasa conv. (eComm.) | Tasa conv. (B2B) |
|---|---|---|---|---|
| Organic Search | 40–50% | 130–200 s | 2,0–3,0% | 1,5–2,5% |
| Paid Search | 50–65% | 100–160 s | 2,0–3,5% | 1,0–2,5% |
| Direct | 40–60% | 80–140 s | 0,5–2,0% | 0,5–1,5% |
| Email | 25–45% | 150–250 s | 1,5–4,0% | 2,0–5,0% |
| Social | 60–80% | 40–80 s | 0,2–1,0% | 0,1–0,5% |
| Referral | 40–60% | 90–160 s | 0,5–2,0% | 0,5–2,0% |

*Fuentes: Contentsquare 2024, Semrush 2024, First Page Sage 2023, Databox GA4 Benchmarks 2024.*

---

## 10. Clasificación de anomalías de tráfico

### Pico de sesiones: ¿bot o evento real?

| Señal | Bot / spam | Campaña / evento real |
|---|---|---|
| Bounce rate | ≥ 0,95 | < 0,95 (puede ser alto, pero no extremo) |
| Duración media | ≤ 5 segundos | > 5 segundos (puede ser baja pero humana) |
| Conversiones | = 0 | > 0 (aunque la tasa sea baja) |
| Recuperación al baseline | Inmediata (1 día) | Puede ser gradual o escalonada |
| Canales afectados | Generalmente 1 (Direct o Referral) | Varios, correlacionados con la campaña |

**Regla operativa:**
- Si las tres señales coinciden (bounce ≥ 0,95 **Y** dur ≤ 5s **Y** conv = 0) → bot con alta probabilidad.
- Si al menos una señal difiere (conv > 0 **O** bounce < 0,95 **O** dur > 5s) → tráfico real, aunque de calidad inferior al baseline. Clasificar como campaña/evento real.
- Tráfico de campaña con bounce alto (0,60–0,80) y duración baja (30–80 s) es normal: el usuario llega por impulso, verifica el producto y se va. No es bot.

**Cálculo de sesiones bot netas:**
Sesiones bot estimadas = sesiones del día pico − media del canal en días normales.
Citar siempre el neto, no solo el bruto del día anómalo.

### Caída de tráfico: ¿tracking break o pérdida real?

| Señal | Tracking break / problema técnico | Pérdida real de audiencia |
|---|---|---|
| Patrón de la caída | Simultánea en todos los canales, mismo día | Gradual o selectiva (un canal o tipo de usuario) |
| Ratio de caída en un día | > 30–40% en 24 h | Raro sin evento externo conocido |
| Métricas de calidad | Estables antes y después (bounce, duración) | Pueden cambiar (peor audiencia → peor calidad) |
| Recuperación espontánea | Sin recuperación (el nuevo nivel es permanente) | Puede recuperarse con acciones de marketing |

### Hueco de datos: ausencia de registros vs. tracking break

| Señal | Hueco de datos (laguna de exportación) | Tracking break |
|---|---|---|
| Filas en el CSV | 0 filas para esas fechas | Filas presentes con valores reducidos |
| Reanudación post-evento | Datos vuelven al nivel pre-hueco | Datos permanecen reducidos de forma permanente |
| Diagnóstico | Corte en exportación o data stream | Cambio en medición (consent, tag, filtro) |

---

## 11. Experimentación: test A/B (imprescindible: decidir con datos, no con opinión)

> Un test A/B convierte *"creemos que B es mejor"* en *"medimos que B es mejor"*. Es el **gold
> standard** para validar un cambio en una web/landing/email (≈92% de fiabilidad causal, ver
> `RAG_Master_IA_M1`). El juicio de copy (rúbrica + escéptico) **propone**; el A/B **decide**.

### 11.1 Cuándo SÍ y cuándo NO
- **SÍ:** hay tráfico suficiente para alcanzar significancia en un plazo razonable y la decisión
  importa (CTA, titular, precio, layout, flujo de registro).
- **NO (y qué hacer):** tráfico bajo → no llegarás a significancia en semanas → usar **tests de
  usabilidad / usuarios simulados / FeedbackLoop + juicio del escéptico**, asumiendo que es decisión
  **cualitativa**, no medida. Nunca decretar un ganador de un test infrapotenciado.

### 11.2 El método, paso a paso
1. **Hipótesis** explícita: *"Si [cambio], entonces [métrica primaria] mejora, porque [insight]."*
   Sin hipótesis no es experimento, es tocar.
2. **UNA métrica primaria** que decide (la que mueve negocio: conversión, clics al CTA, leads) +
   **métrica guardia** (que no empeore: rebote, devoluciones) + secundarias de diagnóstico.
   **Solo la primaria decide.**
3. **Variantes que cambian UNA cosa** (A = control, B = variante). Cambiar titular + color + CTA a
   la vez y ganar = no sabes qué lo causó → eso es multivariante (§11.5), no A/B.
4. **Asignación aleatoria y simultánea** del tráfico (no "esta semana A, la siguiente B" → contamina
   con estacionalidad y eventos).
5. **Tamaño de muestra y duración fijados ANTES** (§11.3).
6. **Leer con significancia** (§11.3) y decidir: adoptar B, quedarse con A, o iterar.

### 11.3 Tamaño de muestra, significancia y duración (lo que más se hace mal)
- El **tamaño de muestra NO es fijo**: depende de (a) la **tasa base** de conversión, (b) el
  **efecto mínimo detectable (MDE)** que te interesa (p. ej. +10% relativo), (c) **nivel de
  confianza** (convención **95%**, α=0,05) y (d) **potencia** (convención **80%**). Menor tasa base
  o menor MDE → más muestra. **Calcúlalo ANTES** con una calculadora (Evan Miller, VWO, Optimizely).
  No se estima a ojo.
- **Significancia (p<0,05) = "probablemente no es azar", NO "es grande/importante".** Mira el
  **intervalo de confianza** del efecto: si cruza el 0, no concluyas.
- **Duración:** cubrir **semanas completas** (mín. 1–2 ciclos semanales) para no sesgar por día de
  la semana; respetar la muestra calculada **aunque "ya se vea claro"**.

### 11.4 Errores que INVALIDAN un test (lista de control)
- **Peeking / parar al primer pico** *(error nº1)*: mirar a diario y detener en cuanto sale
  significativo dispara los falsos positivos. Fija duración/muestra y no toques (o usa métodos
  secuenciales diseñados para mirar).
- **Muestra/duración insuficiente:** test infrapotenciado → "no significativo" ≠ "no hay diferencia".
- **Cambiar varias cosas a la vez** sin ser multivariante → resultado no atribuible.
- **Varias métricas "primarias":** comparaciones múltiples inflan falsos positivos. Una, decidida antes.
- **SRM (Sample Ratio Mismatch):** si el 50/50 esperado sale 55/45, hay bug de asignación → no leas el test.
- **Efecto novedad / estacionalidad / eventos externos** (rebajas, campaña) contaminan.
- **Fuga entre variantes:** el mismo usuario ve A y B (sin *sticky bucketing*) → mide ruido.

### 11.5 Variantes del método
- **A/B:** control vs una variante. El caso por defecto.
- **A/B/n:** varias variantes a la vez (más muestra, reparte el tráfico).
- **Multivariante (MVT):** combinaciones de varios elementos para ver interacciones: **exige mucha
  más muestra**; solo con tráfico alto.
- **Split URL:** dos URLs distintas (rediseños grandes), no cambios en la misma página.

### 11.6 Conexión con las simulaciones de usuario (honestidad)
Los **usuarios simulados** (agentes-perfil recorriendo la web) y el **FeedbackLoop con Playwright**
son un **pre-test cualitativo barato**: descartan variantes claramente malas, cazan fricciones y bugs
y afinan la hipótesis **ANTES** de exponer nada a tráfico real. **NO sustituyen un A/B real:** no dan
significancia estadística ni miden conversión real (un agente no "compra"). Regla: **la simulación
criba; el A/B real con tráfico decide.** Decir siempre cuál de los dos respalda un "B es mejor".

### 11.7 Reparto en el enjambre marketer
- **`contenido-marketer`** genera las **variantes con su hipótesis** (cada variante = un ángulo de §0
  con una predicción).
- **`analitica-marketer`** **diseña y mide** el test (métrica primaria, muestra, significancia, SRM).
- El **escéptico** ataca la lectura: ¿señal o ruido?, ¿hubo *peeking*?, ¿la muestra basta?

*Fuentes (verificar en vivo; convenciones del campo): Kohavi, Tang & Xu, "Trustworthy Online Controlled
Experiments" (2020); CXL Institute; documentación de Optimizely / VWO; Evan Miller (tamaño de muestra
y "How Not To Run an A/B Test", sobre el peeking).*

---

*RAG Métricas Audiencias v1.2 · 11/06/2026 · §11 test A/B (metodología completa: hipótesis, métrica primaria, tamaño de muestra/significancia, errores que invalidan, conexión honesta con las simulaciones). Previos: benchmarks por canal (§9), clasificación de anomalías (§10)*
