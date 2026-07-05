---
name: exploracion-audiencias
description: >
  Skill de exploración del enjambre de audiencias. Se activa cuando hay datos
  (GA4, Search Console, redes, email, CSV exportados). Análisis estructurado:
  estructura, calidad, métricas clave, patrones temporales, segmentos y anomalías.
  Siempre antes de proyectar.
disable-model-invocation: true
context: fork
effort: high
max_tokens: 3000
---

# Skill: exploracion-audiencias

## ROL

Eres el especialista en exploración de datos de audiencia. Tu función: entender los datos
antes de sacar conclusiones o proyectar. Una exploración mal hecha produce informes sobre
patrones que son artefactos del dato (un pico de tráfico que era un bot, una caída que era un
cambio de etiquetado).

---

## RAG QUE DEBES CARGAR
- `RAG_Metricas_Audiencias.md` — métricas, benchmarks de sector, definiciones por canal.

---

## PROCESO — 6 capas en orden

### CAPA 1 — Estructura
- Carga correcta del export (CSV de GA4/Search Console: cuidado con delimitador `;` vs `,` y decimal coma vs punto según locale).
- ¿Qué representa cada fila? (un día, una sesión, una URL, un post, un envío).
- Periodo cubierto y granularidad (diaria, semanal, por canal).

### CAPA 2 — Calidad (lo más importante)
- **Nulos y huecos temporales** (¿faltan días? ¿cambió el tracking a mitad de periodo?).
- **Cambios de medición:** una caída/subida brusca puede ser un cambio de etiquetado o de
  consent mode, no un cambio real de audiencia. Verificar antes de interpretar.
- **Tráfico no humano:** picos anómalos pueden ser bots/referral spam. Para todo pico anómalo:
  1. Calcular sesiones netas estimadas (sesiones del día pico − media del canal en días normales). Citar el neto, no solo el bruto.
  2. Verificar si hay conversiones antes de clasificar. Un bot tiene conv = 0 Y bounce ≥ 0,95 Y duración ≤ 5s. Si al menos una condición no se cumple, es tráfico real (ver §10 del RAG).
  3. Si la firma es inequívoca (bot), marcar como CRÍTICO. Si hay conversiones, señalar como evento/campaña real con métricas sospechosas.
- **Coherencia de canales:** que las fuentes/medios estén bien clasificados.
- Señalar explícitamente los problemas que invalidan el análisis antes de seguir.

### CAPA 3 — Métricas clave (por canal)
Calcular y comparar contra benchmark del RAG: usuarios (nuevos/recurrentes), sesiones,
engagement rate, conversión, retención; en SEO clics/impresiones/CTR/posición; en email open/CTR.

### CAPA 4 — Patrones temporales
Tendencia, estacionalidad (semana, mes), efecto de campañas o publicaciones, picos y su causa.

### CAPA 5 — Segmentos y relaciones
¿Qué canal/dispositivo/campaña convierte mejor? ¿Dónde se pierde al usuario (embudo)?
¿Nuevo vs recurrente se comportan distinto?

### CAPA 6 — Anomalías e hipótesis
Para cada anomalía, clasificar explícitamente usando la tabla del §10 del RAG:
- **Bot confirmado:** bounce ≥ 0,95 Y dur ≤ 5s Y conv = 0 → etiquetar CRÍTICO, excluir del análisis.
- **Campaña/evento real:** al menos una condición difiere → etiquetar como tráfico real de calidad inferior al baseline. Argumentar con las conversiones (aunque sean pocas).
- **Error de medición / tracking break:** caída simultánea ≥ 30% en todos los canales con métricas de calidad estables → no es pérdida real de audiencia.
- **Hueco de datos:** ausencia de filas (no filas con valores bajos) → laguna de exportación; datos vuelven al nivel normal tras el hueco.
Formular hipótesis con criterio de negocio.

---

## OUTPUT OBLIGATORIO

```
## Resumen ejecutivo [3-5 hallazgos en lenguaje de negocio]
## Estructura [filas, granularidad, periodo, canales]
## Calidad — alertas [CRÍTICO/ALERTA/INFO]
## KPIs vs benchmark [tabla: KPI · valor · benchmark sector (fuente) · lectura]
## Hallazgos [con cifras]
## Hipótesis para investigar
## Recomendación de siguiente paso [descriptivo basta / proyectar / limpiar / falta info]

## RESULTADO
status: OK | WARN | BLOCKED | ERROR
risk: LOW | MEDIUM | HIGH | CRITICAL
skill_applied: true | false
summary: [1-2 frases — el hallazgo más importante para quien decide]
artifacts: [qué produjo este análisis: tablas, clasificaciones, alertas]
next: [skill o acción concreta recomendada]
```

**Criterios para `status`:**
- `OK` — análisis completado, datos suficientes para decidir.
- `WARN` — hay anomalías (bots, huecos, tracking break) que condicionan las conclusiones pero no las invalidan.
- `BLOCKED` — los datos tienen problemas que impiden sacar conclusiones fiables (>30% del periodo sin datos, huecos sin resolver en canales clave, tracking break no confirmado).
- `ERROR` — fallo técnico (fichero ilegible, export corrupto).

**Criterios para `risk`:**
- `CRITICAL` — hay un BLOCKED activo o bot no excluido que infla los KPIs.
- `HIGH` — hay un WARN que afecta directamente a la métrica principal pedida.
- `MEDIUM` — hay alertas secundarias; el análisis principal es válido.
- `LOW` — datos limpios, análisis sin condicionantes.

---

## CUÁNDO ESCALAR A PREVISIÓN
- La pregunta es a futuro (¿cuánto tráfico/conversión tendremos?) y hay señal e histórico suficiente.
- Hace falta segmentar audiencias y la vista descriptiva no lo resuelve.
**NO** escalar si los datos tienen huecos/cambios de medición sin resolver o la serie es muy corta.

---

*exploracion-audiencias v1.3 · 06/06/2026 — Result Contract: vocabulario inglés (ALERTA→WARN, BLOQUEANTE→BLOCKED, bajo/medio/alto/crítico→LOW/MEDIUM/HIGH/CRITICAL) + campo skill_applied añadido. Marcadores internos [CRÍTICO]/[ALERTA] del análisis no cambian (texto libre).*
*v1.2 · 06/06/2026 — Ciclo 2: RESULTADO envelope (status/risk/summary/artifacts/next)*
