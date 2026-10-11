# Metodología

## Pregunta de negocio
_¿Dónde se acumulan los tiempos de espera y cómo se pueden reducir?_

## Datos
Tablas utilizadas y su granularidad (visita, etapa, paciente).

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
