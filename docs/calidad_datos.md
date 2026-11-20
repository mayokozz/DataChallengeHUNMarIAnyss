# Calidad de datos

Hallazgos de la exploración del modelo OMOP (cifras reproducibles con `sql/01_exploracion.sql`, `sql/02_calidad_datos.sql` y el notebook EDA).

## Volumen
| Tabla | Filas |
|---|---:|
| person | 912.205 |
| visit_occurrence | 1.706.001 |
| visit_detail | 3.281.613 |
| condition_occurrence | 38.636.063 |
| procedure_occurrence | 47.042.032 |
| measurement | 16.575.888 |
| concept | 10.004.331 |

Tipos de visita: Ambulatory Rehabilitation 1.089.461; ER 598.088; Treatment urgency 17.858; Inpatient 592.

## Hallazgos
| Hallazgo | Detalle | Impacto |
|---|---|---|
| Duración no calculable | `visit_end` = `visit_start` en el 100 % de las visitas; en `visit_detail` start = end en el 100 % | No se pueden medir duraciones ni tiempos de espera |
| Fechas futuras | 82 registros de `condition_occurrence` posteriores a 2026-08-13 (hasta 2033-05-29) | Se usa 2026-08-13 como fin del periodo confiable |
| `procedure_date` | Nulo en el 100 % | No usable |
| `measurement.value_as_number` | Nulo en 38,45 % | Uso limitado |
| `provider_id` | No útil | No se analiza por profesional |
| Años de nacimiento | 87 inválidos | Se excluyen de análisis demográficos |
| Pacientes | 304.457 de 912.205 personas tienen visitas (33,38 %); promedio 5,60 visitas por paciente, mediana 3, máximo 1.218 | Cobertura parcial de la población registrada |
| `visit_detail` | Cubre 95,12 % de las visitas (1 a 34 detalles por visita) | Detalle casi completo |

## Patrones de demanda (histórico)
- Día más alto: miércoles (317.667 visitas); más bajo: domingo (69.490).
- Horas más altas: 9 h (203.266), 8 h (187.996), 10 h (176.637); más bajas: 4 h (5.407), 3 h (5.588), 2 h (6.311).
- Meses más altos: abril (170.102), mayo (169.231), marzo (159.185); más bajos: diciembre (106.179), noviembre (121.268), agosto (127.595).
- Promedio aproximado de 1.310 visitas por día (mínimo 2, máximo 2.795).

## Consecuencia
El análisis se centra en volumen de demanda por hora. Los datos posteriores a 2026-07-17 18:00 se consideran no confiables para evaluación.
