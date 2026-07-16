# audience-analyst-swarm

**Enjambre multi-agente con Claude para analítica de audiencias digitales**
**Multi-agent Claude swarm for digital audience analytics**

[Español](#español) · [English](#english)

---

## Español

### Qué resuelve

Un sistema multi-agente (un "enjambre" de skills especializadas) para analítica de audiencias
digitales, construido sobre un método **ya probado en otros dos dominios**: contabilidad y
análisis de datos. No es una herramienta de producción: es la **estructura completa** de un
enjambre de agentes de dominio, lista para enriquecerse con uso real.

**La idea:** no soy analista de audiencias de carrera. Construyo **sistemas de agentes de IA**
que analizan cualquier dominio con método y rigor. Para demostrarlo monté este enjambre y lo usé
para responder una pregunta real con datos públicos (*el auge de las "skills" de IA*), dejando
que los datos corrigieran mi propia hipótesis.

### Las 5 skills

`orquestador-audiencias` → `discovery-audiencias` → `exploracion-audiencias` → `prevision-audiencias` → `comunicacion-audiencias`

(orquestador → estrategia de medición → exploración de datos → previsión → informe a stakeholders)

### Caso de estudio en vivo: el auge de las "skills" de IA

Ejecuté el enjambre sobre **datos reales de Google Trends**. El interés de búsqueda por las "skills"
de IA se multiplicó **~×80** en ocho meses, despegando con el lanzamiento de **Agent Skills** de
Anthropic (oct-2025).

![Curva de interés de búsqueda](estudio_skills/grafico_tendencia_skills.png)

Hallazgo honesto: mi hipótesis inicial ("plano todo el año, repunte en las últimas 2 semanas") era
**incorrecta**. Los datos mostraron una tendencia estructural de 8 meses, con el pico ya en mayo de
2026. Lo reporto tal cual: en análisis, los datos mandan sobre la intuición. Estudio completo:
[`estudio_skills/ESTUDIO_Skills_Tendencia.md`](estudio_skills/ESTUDIO_Skills_Tendencia.md).

### ~70% reutilizado, ~30% nuevo

El patrón de enjambre, la orquestación, el método de evaluación y la gobernanza se reutilizan del
enjambre de análisis de datos. Solo son nuevos el conocimiento de dominio (métricas y benchmarks de
audiencia) y las 5 skills, por eso un dominio nuevo se levanta en días, no en meses.

### Privacidad

100% portable. El caso de estudio usa **solo datos públicos y agregados** (Google Trends, GitHub).
Sin datos personales ni perfilado: el uso de IA aquí es libre de RGPD. Las skills saben dónde está
la línea entre dato *público/agregado* (libre) y *personal* (RGPD/ePrivacy).

### Estructura

```
audience-analyst-swarm/
  README.md
  arquitectura.md          decisiones de diseño
  Result_Contract.md       cómo cierra cada skill para que el orquestador la entienda
  rag/
    RAG_Metricas_Audiencias.md    métricas + benchmarks (con fuente)
  skills/                  las 5 skills (español)
    orquestador-audiencias/
    discovery-audiencias/
    exploracion-audiencias/
    prevision-audiencias/
    comunicacion-audiencias/
  estudio_skills/          caso de estudio
    ESTUDIO_Skills_Tendencia.md
    grafico_tendencia_skills.png
    trends_skills.py · grafico_trends.py
    google_trends_skills_*.csv
```

### Repos relacionados

Este enjambre es el mismo método aplicado a otro dominio. Las piezas hermanas:

- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): el enjambre contable del que sale el método, con su evaluación continua.
- [orquestacion-enjambres-ia](https://github.com/jleonceo/orquestacion-enjambres-ia): el enrutado, cómo se decide a qué agente va cada petición sin romperse al crecer.
- [gobernanza-skills-analiticas](https://github.com/jleonceo/gobernanza-skills-analiticas): el método que gobierna estos enjambres, con golden sets y puertas de no-regresión.
- [verificacion-determinista-ia](https://github.com/jleonceo/verificacion-determinista-ia): el guardarraíl que recomprueba la coherencia de los datos sin IA.
- [agent-memory-governance](https://github.com/jleonceo/agent-memory-governance): que la memoria del agente no se convierta en un vertedero.
- [llm-eval-contable](https://github.com/jleonceo/llm-eval-contable): de dónde nace todo, la evaluación de una sola skill.

---

## English

### What it solves

A multi-agent system (a "swarm" of specialized skills) for digital audience analytics, built on
a method already proven in two other domains: accounting and data analysis. It's not a
production tool: it's the **complete structure** of a domain-specific agent swarm, ready to be
enriched with real use.

**The point:** I'm not a career audience analyst. I build **AI agent systems** that analyze any
domain with method and rigor. To prove it, I built this one and used it to answer a real
question with public data (*the rise of AI "skills"*), and let the data correct my own
hypothesis.

### The 5 skills

`orquestador-audiencias` → `discovery-audiencias` → `exploracion-audiencias` → `prevision-audiencias` → `comunicacion-audiencias`

(orchestrator → measurement strategy → data exploration → forecasting → stakeholder reporting)

### Live case study: the rise of "AI skills"

I ran the swarm on **real Google Trends data**. Search interest in AI "skills" multiplied **~80×**
in eight months, taking off with Anthropic's **Agent Skills** launch (Oct 2025).

![Search interest curve](estudio_skills/grafico_tendencia_skills.png)

Honest finding: my initial hypothesis ("flat all year, spike in the last 2 weeks") was **wrong**.
The data showed an 8-month structural trend, with the peak already in May 2026. I report it as
it is: in analytics, data beats intuition. Full study: [`estudio_skills/ESTUDIO_Skills_Tendencia.md`](estudio_skills/ESTUDIO_Skills_Tendencia.md).

### ~70% reused, ~30% new

The swarm pattern, orchestration, evaluation method and governance are reused from the data-analysis
swarm. Only the domain knowledge (audience metrics & benchmarks) and the 5 skills are new, which is
why a new domain can be stood up in days, not months.

### Privacy

100% portable. The case study uses **only public, aggregated data** (Google Trends, GitHub). No
personal data, no profiling: AI use here is free of GDPR constraints. The skills know where the
line is between *public/aggregated* (free) and *personal* (GDPR/ePrivacy).

### Structure

```
audience-analyst-swarm/
  README.md
  arquitectura.md          design decisions
  Result_Contract.md       how each skill signs off so the orchestrator can read it
  rag/
    RAG_Metricas_Audiencias.md    metrics + benchmarks (with source)
  skills/                  the 5 skills (in Spanish)
    orquestador-audiencias/
    discovery-audiencias/
    exploracion-audiencias/
    prevision-audiencias/
    comunicacion-audiencias/
  estudio_skills/          case study
    ESTUDIO_Skills_Tendencia.md
    grafico_tendencia_skills.png
    trends_skills.py · grafico_trends.py
    google_trends_skills_*.csv
```

### Related repositories

This swarm is the same method applied to a different domain. Its sibling projects:

- [accounting-agent-swarm](https://github.com/jleonceo/accounting-agent-swarm): the accounting swarm the method comes from, with its continuous evaluation.
- [orquestacion-enjambres-ia](https://github.com/jleonceo/orquestacion-enjambres-ia): the routing, how a system decides which agent handles each request without breaking as it grows.
- [gobernanza-skills-analiticas](https://github.com/jleonceo/gobernanza-skills-analiticas): the method that governs these swarms, with golden sets and no-regression gates.
- [verificacion-determinista-ia](https://github.com/jleonceo/verificacion-determinista-ia): the guardrail that rechecks the coherence of the data without AI.
- [agent-memory-governance](https://github.com/jleonceo/agent-memory-governance): keeping the agent's memory from turning into a junkyard.
- [llm-eval-contable](https://github.com/jleonceo/llm-eval-contable): where it all started, the evaluation of a single skill.

---

*audience-analyst-swarm · prueba de concepto / proof of concept · 04/06/2026 · Licencia / License: [MIT](LICENSE)*
