# Modelo de pronóstico de demanda por hora

## Descripción
Random Forest que predice el número de visitas por hora para un horizonte de 168 horas (7 días).

**Variables:** hora, día de la semana, mes, indicador de fin de semana, rezago de 168 h, rezago de 336 h y media móvil de 168 h.

**Entrenamiento:** datos hasta 2026-07-16 23:00. Los datos posteriores a 2026-07-17 18:00 se marcaron como no confiables.

**Salida:** archivo CSV por hora (`hourly_demand_forecast`) con `visit_start_datetime` y `Predicted_Demand`. Son estimaciones puntuales, sin intervalos de confianza. El pronóstico es retrospectivo (17–23 de julio de 2026). El CSV **no** se sube al repositorio.

## Línea base
Valor de la misma hora de la semana anterior (estacional ingenuo).

## Resultados globales
| Métrica | Random Forest | Línea base |
|---|---:|---:|
| MAE (visitas/hora) | 13,57 | 18,09 |
| RMSE (visitas/hora) | 27,69 | 36,68 |
| R² | 0,771 | 0,598 |

## Evaluación semanal
| Semana | MAE RF | MAE línea base | RMSE RF | R² RF |
|---|---:|---:|---:|---:|
| 1 | 12,676 | 18,310 | 22,111 | 0,861 |
| 2 | 15,659 | 18,155 | 33,181 | 0,597 |
| 3 | 10,339 | 17,417 | 17,126 | 0,921 |
| 4 | 15,601 | 18,488 | 34,416 | 0,650 |

## Limitaciones
- Evaluación retrospectiva sobre una sola ventana temporal.
- Sin intervalos de incertidumbre.
- Los resultados dependen de la calidad de los datos recientes (ver `docs/calidad_datos.md`).
