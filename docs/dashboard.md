# Dashboard interactivo (Power BI)

El proyecto (`.pbip`) tiene siete páginas con la paleta institucional (Slate Grey 5F758E, Prussian Blue 00072D, Dark Raspberry 89023E, Ghost White EDEDF4, Carbon Black 1B2021) y fuente DIN. Cada página responde una pregunta.

## Guía por página
### 1. Resumen — «¿De qué trata el proyecto?»
- **Muestra:** cifras clave, visitas por tipo, propósito y advertencia de alcance.
- **Cómo leerla:** es la portada; da el contexto antes de entrar al detalle.
- **No concluir:** que las cifras históricas predicen por sí solas la demanda futura.

### 2. Datos y calidad — «¿Qué tan buenos son los datos?»
- **Muestra:** filas por tabla OMOP y hallazgos de calidad (qué falla y qué impacto tiene).
- **Cómo leerla:** cada hallazgo explica qué se pudo y qué no se pudo analizar.
- **Clave:** la duración de las visitas no es calculable, por eso se mide demanda por hora y no tiempos de espera.

### 3. Patrones de demanda — «¿Cuándo llegan los pacientes?»
- **Muestra:** visitas esperadas por hora del día y por día; mosaicos con día, hora y mes más y menos cargados (histórico 2023–2026).
- **Cómo leerla:** barras altas = más pacientes. Hay picos entre 8 y 10 h y casi no hay llegadas de madrugada.
- **No concluir:** causas de los picos; solo se describen.

### 4. Modelo predictivo — «¿Qué tan bien se pronostica?»
- **Muestra:** error promedio (MAE), mejora frente a la línea base, ajuste (R²), pronóstico por hora y error por semana.
- **Cómo leerla:** error más bajo es mejor; barra oscura = modelo, barra gris = línea base. Un R² de 0,77 indica que sigue bien el patrón (1 sería perfecto).
- **No concluir:** que el modelo sea válido para cualquier fecha; se evaluó en una sola ventana (17–23 jul 2026).

### 5. Simulador — «¿Alcanzaría el personal?»
- **Muestra:** 4 controles (cambio de demanda y personal de mañana, tarde y noche), 4 tarjetas, curva de demanda vs. capacidad y el asistente.
- **Cómo leerla:** si la línea roja (demanda) pasa sobre la oscura (capacidad), falta personal en esa hora.
- **No concluir:** que la sugerencia sea un plan óptimo o que reduzca esperas.

### 6. Recomendaciones — «¿Qué hacemos con esto?»
- **Muestra:** comparación, por hora del día, de la demanda esperada con la capacidad de dos planes con el mismo personal (turnos fijos vs. escalonados), y cuatro acciones propuestas.
- **Cómo leerla:** la curva oscura (turnos escalonados) sigue mejor a la curva roja (demanda) que la gris (turnos fijos).
- **No concluir:** que el plan escalonado sea el óptimo ni que reduzca esperas; es un escenario con supuestos ficticios. Detalle en `docs/resultados_y_recomendaciones.md`.

### 7. Metodología — «¿Cómo se hizo y qué límites tiene?»
- **Muestra:** datos, pasos, supuestos, limitaciones y reproducibilidad.
- **Cómo leerla:** léela antes de usar los resultados para decidir.

## Fuentes dentro del modelo
- Pronóstico horario: CSV local (no versionado).
- Tablas de documentación (métricas, evaluación semanal, tipos de visita, tablas OMOP, extremos históricos): tablas calculadas con valores tomados de este repositorio.

## Enlace
Dashboard publicado: [abrir en Power BI](https://app.powerbi.com/groups/me/reports/e0e62a33-0c3e-4946-b184-40f047c25f80?ctid=bab0b679-bd5f-4fe8-b516-c6b8b317c782&pbi_source=linkShare)

## Abrir el proyecto
`powerbi/HUN_Dashboard.pbip` se abre con Power BI Desktop (activar la vista previa de «Power BI Project» si lo pide). La fuente del pronóstico apunta a `C:\ruta\a\hourly_demand_forecast.csv`: cambia la ruta a tu CSV local (Transformar datos → Configuración de origen) y presiona «Actualizar». Si Power BI avisa que hay tablas calculadas por actualizar, presiona «Actualizar ahora».
