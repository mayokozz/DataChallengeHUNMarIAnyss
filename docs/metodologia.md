# Metodología

## Pregunta de negocio
_¿Dónde se acumulan los tiempos de espera y cómo se pueden reducir?_

## Datos
Esquema `uninorte_omop` (OMOP CDM). Cantidad de registros por tabla:

| Tabla  | Filas | Qué representa cada fila |
|---|--- |---    |
| person |912205 | Un paciente anonimizado |

| visit_occurrence| 1706001| Una visita o encuentro clínico |

| visit_detail | 3281613| Una etapa dentro de una visita |

| condition_occurrence |38636063 | Un diagnóstico registrado |

| procedure_occurrence |47042032| Un procedimiento realizado |

| measurement | 16575888| Una medición o laboratorio |

| concept |10004331| Un concepto del diccionario de vocabularios |.
DATO 2 --- PERIODO DE LOS DATOS
Los datos van desde 2023-01-01 00:21:55.000 hasta 2026-08-13 15:20:00.000
DATO 3 - TIPOS DE VISITAS
|tipo de visita| | numero de visitas |
|Ambulatory Rehabilitation Visit |   | 1089461 |
|Emergency Room Visit |             | 598088| 
| Treatment urgency {Diagnosis}|         |17858 |
| Inpatient Visit|        |592 |
## Limpieza
Ver `decisiones_limpieza.md`.

## Métricas definidas
- Duración de visita = visit_end - visit_start
- Duración de etapa = visit_detail_end - visit_detail_start
- Espera entre etapas = inicio de etapa - fin de la etapa anterior

## Modelo
Variable objetivo, variables predictoras, validación y métricas.

## Resultados y recomendaciones
_Pendiente_
