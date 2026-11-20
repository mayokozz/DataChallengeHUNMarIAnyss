# Metodología

Proyecto del **Data Challenge PRO HUN 2026** (Universidad del Norte × Fundación Hospital Universidad del Norte).

## 1. Pregunta y objetivo
**Pregunta:** ¿cuándo llegan los pacientes y qué tan preparada estaría una dotación de personal para atenderlos?

**Objetivo:** (1) entender los patrones de llegada, (2) pronosticar la demanda por hora para los próximos 7 días y (3) ofrecer un simulador para explorar escenarios hipotéticos de personal por turno.

## 2. Datos y alcance
| Elemento | Detalle |
|---|---|
| Fuente | Modelo de datos OMOP del hospital (`visit_occurrence`, `visit_detail`, `person`, `condition_occurrence`, `procedure_occurrence`, `measurement`, `concept`) |
| Periodo | 2023-01-01 a 2026-08-13 |
| Unidad de análisis | Visita (una fila de `visit_occurrence`) |
| Privacidad | Los datos y las credenciales **no** se publican en el repositorio |

## 3. Flujo de trabajo
| Paso | Qué se hizo | Dónde está |
|---|---|---|
| 1. Exploración | Conteo de tablas, tipos de visita, patrones por hora, día y mes | `sql/01_exploracion.sql`, `notebooks/eda_visits_occurrence.ipynb` |
| 2. Calidad de datos | Revisión de fechas, nulos y consistencia | `sql/02_calidad_datos.sql`, `docs/calidad_datos.md` |
| 3. Duración y espera | Se intentó calcular; no es posible porque inicio = fin en el 100 % de las visitas | `sql/03`, `sql/04` |
| 4. Pronóstico | Random Forest por hora, comparado con una línea base | `docs/modelo_pronostico.md` |
| 5. Simulador y dashboard | Compara demanda pronosticada con capacidad hipotética por turno | `docs/simulador_capacidad.md`, `docs/dashboard.md` |
| 6. Optimización y recomendaciones | Turnos escalonados con el mismo personal (programación entera) y acciones propuestas | `src/optimizacion_turnos.py`, `docs/resultados_y_recomendaciones.md` |

## 4. Decisiones metodológicas
1. **Medida de demanda = visitas por hora** (según `visit_start_datetime`). Se eligió así porque la duración de las visitas no es calculable.
2. **Fin del periodo confiable = 2026-08-13**, por registros con fechas futuras. Los datos posteriores a 2026-07-17 18:00 se marcaron como no confiables para evaluar.
3. **Línea base = misma hora de la semana anterior.** El modelo solo vale la pena si la supera; lo hace (MAE 13,57 vs. 18,09 visitas/hora, un 25 % menos de error).
4. **Simulador con supuestos explícitos y fijos:** 4 pacientes por hora por profesional y 80 % de utilización. Son hipotéticos, no datos del hospital.
5. **Turnos:** mañana 6–14 h, tarde 14–22 h, noche 22–6 h.

## 5. Cómo se calcula el simulador (resumen)
- Capacidad por hora = profesionales del turno × 4 × 0,8.
- Demanda por hora = pronóstico × (1 + cambio de demanda %).
- Déficit = máx(0, demanda − capacidad). Demanda cubierta = 1 − déficit / demanda total.
- Detalle en `docs/simulador_capacidad.md`.

## 6. Cómo leer los resultados
- El pronóstico dice **cuántas visitas se esperan**, no cuántas se atenderán.
- El simulador dice **dónde la capacidad hipotética no alcanza** con los supuestos elegidos.
- El asistente es una guía por reglas (no es IA) y sus sugerencias son hipótesis.

## 7. Limitaciones (qué NO se puede afirmar)
- No se demuestra reducción real de tiempos de espera.
- No se identifican turnos óptimos.
- No se prueba un aumento de pacientes atendidos.
- El pronóstico es retrospectivo (17–23 de julio de 2026), de una sola ventana y sin intervalos de confianza.
- La capacidad por profesional y la dotación por turno no provienen de datos del hospital.
- Solo el 33,38 % de las personas registradas tiene visitas (cobertura parcial).

## 8. Reproducibilidad
1. Ejecutar los scripts de `sql/` y el notebook sobre una copia local de los datos.
2. Generar el CSV de pronóstico por hora (`visit_start_datetime`, `Predicted_Demand`) y guardarlo fuera del repositorio.
3. Abrir el proyecto de Power BI, apuntar a ese CSV y presionar «Actualizar».

## 9. Trabajo futuro
Intervalos de incertidumbre, validación en más de una ventana, variables externas (feriados, clima) y datos reales de dotación y espera, si el hospital los registra.
