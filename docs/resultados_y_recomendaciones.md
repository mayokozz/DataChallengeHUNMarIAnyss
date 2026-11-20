# Resultados, conclusiones y recomendaciones

> **Alcance.** Los datos no permiten medir tiempos de espera ni validar mejoras reales (la hora de fin de la visita es igual a la de inicio en el 100 % de los casos). Por eso todo lo que sigue es un **ejercicio de escenarios** sobre la demanda pronosticada, con capacidad **hipotética**. Sirve para decidir qué probar y qué medir, no para afirmar mejoras ya comprobadas.

## 1. Qué encontramos (en lenguaje simple)
| # | Hallazgo | Evidencia |
|---|---|---|
| 1 | La demanda tiene **dos picos al día**: 8–11 h y 14–16 h, con una caída a las 12 h | Pronóstico: promedio 143 visitas a las 8 h, 58 a las 12 h y 120 a las 14 h |
| 2 | De madrugada casi no llegan pacientes | 4–5 visitas por hora entre las 1 y las 4 h |
| 3 | El miércoles es el día más cargado y el domingo el más tranquilo (histórico 2023–2026) | 317.667 vs. 69.490 visitas |
| 4 | El pronóstico supera a la línea base | Error promedio 13,6 vs. 18,1 visitas por hora (25 % menos); R² 0,77 |
| 5 | La falta de personal aparece en **ventanas concretas**, no a lo largo del día | Con el plan fijo del simulador (40/30/10): 8–11 h y 14–16 h; lunes, miércoles y jueves; fin de semana sin déficit |
| 6 | El segundo pico (14 h) coincide con el **cambio de turno** y con un turno de tarde más pequeño (30) que el de mañana (40) | Déficit a las 14 h y 15 h comparable al de las 8–10 h |
| 7 | No se pueden medir esperas ni duraciones con los datos actuales | `visit_end` = `visit_start` en el 100 % de las visitas |

## 2. Cuellos de botella (cuando la demanda supera la capacidad hipotética)
Con 40 profesionales de mañana, 30 de tarde y 10 de noche, 4 pacientes por hora y 80 % de uso:
- 33 de 168 horas con déficit; demanda cubierta: 82,6 %.
- Horas críticas: 8, 9, 10 y 11 h (mañana) y 14 y 15 h (inicio de tarde).
- Día de mayor déficit en la semana pronosticada: lunes (20 jul), seguido de miércoles y jueves.

## 3. Propuesta de optimización (hipotética): turnos escalonados
**Idea.** En vez de tres bloques fijos (6, 14 y 22 h), repartir los mismos turnos de 8 horas en distintas horas de inicio, siguiendo la curva de demanda.

**Cómo se calculó.** Programación entera (`src/optimizacion_turnos.py`): se reparten 80 turnos de 8 h (el mismo personal del plan fijo: 40 + 30 + 10) entre las 24 horas de inicio para minimizar el déficit de visitas del pronóstico.

| Plan | Personal (turnos de 8 h) | Demanda cubierta | Horas con déficit (de 168) |
|---|---:|---:|---:|
| Fijo: 40 (6 h), 30 (14 h), 10 (22 h) | 80 | 82,6 % | 33 |
| Escalonado propuesto | 80 | 97,1 % | 20 |

**Inicios de turno propuestos (hora de inicio: profesionales):** 1 h: 2 · 2 h: 1 · 6 h: 9 · 7 h: 19 · 8 h: 23 · 9 h: 12 · 10 h: 3 · 11 h: 4 · 13 h: 1 · 15 h: 2 · 16 h: 1 · 17 h: 3.

**Lectura práctica.** Unos 63 de los 80 turnos empiezan entre las 6 y las 9 h para cubrir el primer pico; el resto cubre el segundo pico y la noche con equipos pequeños.

**Cómo leerlo con cuidado.**
- Es una semana retrospectiva (17–23 jul 2026) y supuestos ficticios; no es un plan óptimo validado.
- No incluye mínimos de seguridad (por ejemplo, un mínimo de personal nocturno), descansos, tipos de servicio ni complejidad de pacientes.
- La noche queda con 2 a 4 profesionales en este ejercicio; el hospital debería fijar su mínimo real antes de usar algo parecido.

## 4. Recomendaciones accionables
| # | Recomendación | Por qué | Cómo probarla | Indicador de éxito |
|---|---|---|---|---|
| R1 | **Escalonar los inicios de turno** para cubrir 8–11 h y 14–16 h | El escenario sube la cobertura de 82,6 % a 97,1 % con el mismo personal | Piloto de 2–4 semanas en un servicio, comparando con el esquema actual | Tiempo de espera y porcentaje de horas con sobrecarga |
| R2 | **Reforzar lunes, miércoles y jueves** en las horas pico | Concentran el déficit de la semana pronosticada; el fin de semana no tiene déficit | Ajustar refuerzos por día con el pronóstico semanal | Déficit estimado frente a atenciones registradas |
| R3 | **Escalonar descansos y almuerzos alrededor de las 12 h** | La demanda cae a ~58 visitas/h entre los dos picos | Programar pausas en esa ventana y evitar pausas a las 8–11 h y 14–16 h | Cobertura en las horas pico |
| R4 | **Revisar la dotación nocturna** | En el escenario fijo, 10 profesionales de noche frente a una necesidad de 2–6 bajo los supuestos | Evaluar con el hospital el mínimo seguro y reasignar el excedente a los picos | Ocupación nocturna y seguridad del servicio |
| R5 | **Registrar horas reales de llegada, triaje, atención y salida** | Sin ellas no se pueden medir esperas ni validar ninguna mejora | Corregir la captura del fin de visita y agregar marcas de tiempo por etapa | `visit_end` distinto de `visit_start`; tiempo entre etapas |
| R6 | **Usar el pronóstico semanalmente** y compararlo con lo observado | El modelo es retrospectivo y de una sola ventana | Reemplazar el CSV cada semana y medir el error real | MAE semanal frente a la línea base |
| R7 | **Medir la capacidad real por profesional** | El valor de 4 pacientes/hora y 80 % de uso es un supuesto | Estudio de tiempos con el equipo asistencial | Capacidad medida por servicio |

## 5. Plan de validación propuesto
1. Corregir y completar la captura de datos (R5).
2. Fijar con el hospital la capacidad real y los mínimos de personal (R7, R4).
3. Piloto controlado del esquema escalonado (R1) en un servicio.
4. Comparar antes y después con los indicadores de la tabla y ajustar el modelo (R6).

## 6. Conclusiones
- La demanda de pacientes sigue un patrón claro por hora y por día, y es predecible con un error 25 % menor que una línea base simple.
- El problema operacional no es la cantidad total de personal sino **cuándo** está disponible: el déficit se concentra en dos ventanas horarias y en pocos días.
- Alinear los turnos con la curva de demanda es la palanca más prometedora del escenario analizado, pero hay que validarla con datos reales de espera.
- El mayor límite del proyecto es de datos, no de método: sin horas reales de atención no se pueden medir cuellos de botella ni mejoras de tiempo.

## 7. Qué NO afirmamos
No afirmamos reducción real de tiempos de espera, turnos óptimos validados ni aumento comprobado de pacientes atendidos. UNINORTE y los participantes no garantizan la aplicabilidad de estas propuestas; la decisión de implementar corresponde al hospital.
