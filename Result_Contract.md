# Result Contract

> Cómo cierra su respuesta cada skill del enjambre para que el orquestador la entienda.
>
> Los valores enumerados (`status`, `risk`) van en inglés para que los pueda parsear código
> (Python, n8n). Los textos libres van en español, que es quien los lee es una persona.

Sin esto, un enjambre no es un enjambre: es un grupo de agentes que producen texto y nadie
sabe si el siguiente puede fiarse del anterior. El contrato es lo que convierte una respuesta
en algo sobre lo que se puede decidir.

## El contrato

Toda skill cuyo resultado necesite leer otro agente cierra con este bloque:

```
## RESULTADO
status: OK | WARN | BLOCKED | ERROR
risk: LOW | MEDIUM | HIGH | CRITICAL
skill_applied: true | false
summary: [1-2 frases: qué se hizo y qué se encontró, para quien decide]
artifacts: [qué se generó o modificó en este paso]
next: [skill o acción concreta recomendada]
```

## Criterios para `status`

| Valor | Cuándo usarlo |
|---|---|
| `OK` | El paso completó correctamente. Hay resultado suficiente para continuar. |
| `WARN` | Hay anomalías que condicionan las conclusiones pero no las invalidan. Se puede continuar con precaución. |
| `BLOCKED` | Hay problemas que impiden sacar conclusiones fiables. No se continúa sin intervención humana. |
| `ERROR` | Fallo técnico o datos ilegibles. El flujo se detiene. Nunca avanzar con ERROR. |

## Criterios para `risk`

| Valor | Cuándo usarlo |
|---|---|
| `LOW` | Datos limpios, análisis sin condicionantes, todos los checks OK. |
| `MEDIUM` | Hay alertas secundarias que afectan al resultado pero no lo invalidan. |
| `HIGH` | Hay un WARN que afecta directamente a la métrica o decisión principal pedida. |
| `CRITICAL` | Hay un BLOCKED activo, o un bot o error no excluido que está inflando los KPIs. |

## El campo `skill_applied`

- `true`: el agente siguió la skill tal como está definida.
- `false`: el agente improvisó, o usó la skill solo como referencia parcial.

Si `skill_applied: false` se repite en el mismo tipo de caso, el problema no es el agente:
es la skill, y necesita revisión. Por eso el campo existe.

## Qué hace el orquestador con esto

| Combinación | Acción |
|---|---|
| `status: OK` + `risk: LOW` | Continúa al siguiente paso. |
| `status: OK` + `risk: MEDIUM` | Continúa, pero registra la advertencia en el resumen final. |
| `status: WARN` (cualquier risk) | Avisa a la persona con el `summary` antes de continuar. Decide ella. |
| `status: BLOCKED` (cualquier risk) | Para. Muestra el `summary`. No continúa sin confirmación explícita. |
| `risk: HIGH` o `CRITICAL` | Para, sea cual sea el status. |
| `status: ERROR` | Para inmediatamente. |
| `skill_applied: false` | No bloquea, pero el orquestador lo menciona al resumir. |

**Regla general:** ante la duda entre WARN y BLOCKED, se usa BLOCKED. Es mejor parar y
preguntar que avanzar con datos infiables.

## Coherencia entre la prosa y lo estructurado

Si una skill emite texto libre y un campo estructurado, los dos dicen lo mismo. El caso
prohibido es que la prosa advierta de algo y el campo estructurado haga lo contrario: quien
lee aguas abajo es código, y el código lee el campo, no la prosa. Una contradicción silenciosa
ahí se convierte en un dato malo tres pasos más allá.

## Ejemplos

```
## RESULTADO
status: OK
risk: LOW
skill_applied: true
summary: Exploración completada sobre Q1 2024 (91 días, 6 canales). Datos limpios. Organic Search lidera conversiones (2,27%). Sin anomalías relevantes.
artifacts: Análisis 6 capas, KPIs por canal vs benchmark, tabla de hallazgos
next: Datos listos para proyección. Activar prevision-audiencias si el objetivo es a futuro.
```

```
## RESULTADO
status: WARN
risk: HIGH
skill_applied: true
summary: Tracking break detectado el 15-feb: los datos posteriores representan solo el 39% del tráfico real. El análisis pre-break (45 días) es válido; la comparación con el post-break no lo es.
artifacts: Análisis 6 capas; KPIs pre-break limpios; cuantificación del tracking break (-61%)
next: Diagnóstico técnico del tracking break (auditoría de GTM/GA4) antes de continuar.
```

El segundo es el que enseña de verdad para qué sirve el contrato. La skill hizo su trabajo
(`skill_applied: true`) y el análisis existe, pero una parte no se puede usar. Sin este bloque,
el siguiente agente cogería los KPIs post-break y proyectaría sobre un dato roto, y nadie se
enteraría hasta que la decisión ya estuviera tomada.

---

*Este documento es la versión local del contrato, autocontenida para este repo. En el sistema
del que sale, el mismo contrato lo comparten varios enjambres.*
