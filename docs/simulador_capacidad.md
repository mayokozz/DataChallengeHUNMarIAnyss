# Simulador de capacidad (Power BI)

## Qué hace
Compara la demanda horaria pronosticada con la capacidad que ofrecería una dotación de profesionales por turno, bajo supuestos hipotéticos ajustables.

## Entradas (parámetros)
| Parámetro | Valor por defecto | Nota |
|---|---:|---|
| Ajuste de demanda (%) | 0 | Escenario «qué pasaría si» sobre el pronóstico (−30 % a +50 %) |
| Pacientes por hora por profesional | 4 (fijo) | Supuesto hipotético, ya no es un control |
| Utilización objetivo | 80 % (fijo) | Supuesto hipotético, ya no es un control |
| Profesionales turno mañana (6–14 h) | 40 | Supuesto hipotético |
| Profesionales turno tarde (14–22 h) | 30 | Supuesto hipotético |
| Profesionales turno noche (22–6 h) | 10 | Supuesto hipotético |

## Cálculos
- Capacidad por profesional por hora = pacientes por hora × utilización.
- Capacidad de la hora = profesionales del turno × capacidad por profesional.
- Demanda de la hora = demanda pronosticada × (1 + ajuste/100).
- Déficit de la hora = máx(0, demanda − capacidad).
- Demanda cubierta (%) = (demanda total − déficit total) / demanda total.
- Profesionales necesarios en la hora pico = ⌈demanda pico / capacidad por profesional⌉.

## Salidas
Cuatro tarjetas (visitas esperadas, demanda cubierta, horas con déficit, personal extra en el pico), una curva de demanda vs. capacidad por hora y un asistente.

## Asistente del simulador
Es un conjunto de respuestas basadas en reglas (medidas DAX), **no** un modelo de lenguaje. Se actualiza con los controles y responde: ¿dónde falta personal?, ¿qué hora es más crítica?, ¿cuántos más haría falta? y ¿dónde sobra capacidad?, y propone una sugerencia hipotética con cantidad: cuántos profesionales mover del turno con holgura al turno con déficit (sin dejar al turno de origen corto en su hora pico) y cuántos faltarían aún como refuerzo. Si ningún turno tiene personal de sobra, sugiere solo sumar refuerzo.

## Advertencia
La capacidad por profesional y la dotación por turno **no** son datos del hospital. El simulador sirve para explorar escenarios; no demuestra reducción de esperas ni identifica turnos óptimos.

## Actualización
Reemplazar el CSV de pronóstico en la misma ruta y presionar «Actualizar» en Power BI. No subir el CSV al repositorio.
