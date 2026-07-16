# Arquitectura: Enjambre Analista de Audiencias

*Decisiones de diseño · 04/06/2026*

---

## Estado: ESTRUCTURA / PRUEBA DE CONCEPTO

Mismo punto de partida desde el que nacieron los enjambres contable y de analista de datos:
estructura completa, lista para enriquecerse con uso y datos reales. No es producción.

---

## Decisión: enjambre (no skill única)

Igual que en el analista de datos, el dominio de audiencias es demasiado amplio para una skill
única sin quedar superficial: medición estratégica, exploración de datos de canal, previsión y
comunicación a negocio son tareas distintas. Se replica el patrón de enjambre ya validado.

## Las 5 skills

| Skill | Función | Espejo de |
|---|---|---|
| `orquestador-audiencias` | Punto de entrada: diagnostica la petición de medición y coordina. | orquestador-analista |
| `discovery-audiencias` | Traduce objetivos de negocio en KPIs y plan de medición (+ guía de etiquetado). | discovery-analista |
| `exploracion-audiencias` | Explora e interpreta datos de audiencia (web, SEO, redes, email). | eda-analista |
| `prevision-audiencias` | Proyección de tráfico/conversión y segmentación cuando hace falta. | modelado-analista |
| `comunicacion-audiencias` | Informe y cuadro de mando para stakeholders, con comparación vs benchmark. | comunicacion-analista |

Flujo: **orquestador → discovery → exploración → (previsión si aplica) → comunicación.**

---

## Reglas de oro, a fuego en el enjambre (no negociables)

1. **Datos públicos y agregados por defecto.** Trends, benchmarks de sector, conversación
   pública. No se perfila a individuos.
2. **Privacidad consciente:** distinguir SIEMPRE dato público/agregado (uso libre) de dato
   personal (GA4 con ID, cookies, CRM, email → RGPD/ePrivacy aplican). Si aparece dato
   personal, marcar la restricción antes de continuar.
3. **Verificar antes de afirmar.** Toda cifra con fuente. Nunca inventar benchmarks ni tendencias.
4. **Nunca tocar el dato original.** Trabajar sobre copia. El fichero/fuente es de solo lectura.
5. **Los datos mandan sobre la hipótesis.** Si los datos refutan lo que esperábamos, se reporta.

---

## Qué se reutiliza (el ~70%)

- Patrón de enjambre y orquestación con plan en voz alta.
- Método de exploración por capas (estructura → calidad → distribuciones → relaciones → anomalías).
- Criterio de cuándo escalar a previsión y cuándo no.
- Filosofía de evals y verificación.

## Qué es nuevo (el ~30%)

- `RAG_Metricas_Audiencias.md`: métricas y benchmarks de dominio (web, SEO, redes, email).
- Las 5 skills especializadas en medición de audiencias.

---

## Privacidad y portabilidad

100% portable: sin datos de ninguna empresa, sin credenciales. El caso de estudio incluido
(`estudio_skills/`) usa exclusivamente datos **públicos y agregados** (Google Trends, GitHub).

---

*Enjambre Analista de Audiencias · arquitectura v1.0 · 04/06/2026*
