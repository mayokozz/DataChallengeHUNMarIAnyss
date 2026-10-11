# Data Challenge HUN 2026 — Flujo de pacientes

Proyecto desarrollado para el Data Challenge HUN 2026 (Universidad del Norte en cooperación con la Fundación Hospital Universidad del Norte).

> **Este repositorio no contiene datos ni credenciales.** Los datos son confidenciales y solo se usan para el reto.

## 1. Problema
Comprender, predecir y optimizar el flujo de pacientes, identificando cuellos de botella y oportunidades de mejora en los tiempos de atención.

## 2. Enfoque (resumen)
1. Exploración y calidad de datos (`sql/01`, `sql/02`).
2. Métricas de flujo: duración de visitas y etapas (`sql/03`, `sql/04`).
3. Modelo predictivo (`notebooks/`, `src/`).
4. Propuestas de mejora operacional (`docs/`).
5. Dashboard interactivo en Power BI (enlace abajo).

## 3. Estructura
```
sql/         consultas numeradas, en orden de ejecución
src/         código reutilizable (conexión, limpieza, features, modelo)
notebooks/   análisis exploratorio y modelado
docs/        metodología, decisiones de limpieza, diccionario de variables
data/        vacío (ver data/README.md)
```

## 4. Cómo reproducir
1. Clonar el repositorio y crear el entorno:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Copiar `.env.example` a `.env` y completar credenciales propias (provistas por la organización).
3. Ejecutar las consultas de `sql/` en orden.
4. Ejecutar los notebooks de `notebooks/` en orden.

## 5. Dashboard
Enlace al dashboard Power BI: _pendiente_

## 6. Equipo
_Nombres de los integrantes_

## 7. Documentación
Ver `docs/metodologia.md` y `docs/decisiones_limpieza.md`.
