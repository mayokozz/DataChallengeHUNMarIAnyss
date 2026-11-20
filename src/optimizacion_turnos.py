"""Propuesta HIPOTÉTICA de turnos escalonados a partir del pronóstico horario.

Pregunta: con la MISMA cantidad de personal (misma cantidad de turnos de 8 h),
¿qué tanto mejora la cobertura de la demanda pronosticada si los turnos
empiezan a distintas horas en lugar de tres bloques fijos (6, 14 y 22 h)?

Supuestos (hipotéticos, NO son datos del hospital):
  - Cada profesional atiende 4 pacientes/hora y se usa al 80 % -> 3,2 visitas/hora.
  - Todos los turnos duran 8 horas y pueden empezar en cualquier hora.
  - Se compara contra el plan fijo del simulador: 40 (6-14), 30 (14-22) y 10 (22-6).

Uso:
    python src/optimizacion_turnos.py ruta/al/hourly_demand_forecast.csv

El CSV (visit_start_datetime, Predicted_Demand) NO se sube al repositorio.
Es un ejercicio de escenarios sobre una semana retrospectiva, no un plan
óptimo validado ni una prueba de reducción de esperas.
"""
import sys

import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp

CAPACIDAD_POR_PROFESIONAL = 4 * 0.8
DURACION_TURNO = 8
PLAN_FIJO = {6: 40, 14: 30, 22: 10}


def matriz_cobertura(duracion=DURACION_TURNO):
    """A[h, s] = 1 si un turno que empieza en la hora s cubre la hora h."""
    a = np.zeros((24, 24))
    for s in range(24):
        for k in range(duracion):
            a[(s + k) % 24, s] = 1
    return a


def evaluar(demanda, horas, inicio_a_personal):
    """Cobertura y déficit del pronóstico para un plan {hora_inicio: profesionales}."""
    a = matriz_cobertura()
    x = np.zeros(24)
    for s, n in inicio_a_personal.items():
        x[s] = n
    capacidad_hora = (a @ x) * CAPACIDAD_POR_PROFESIONAL
    deficit = np.maximum(0, demanda - capacidad_hora[horas])
    return {
        "cobertura": 1 - deficit.sum() / demanda.sum(),
        "deficit_visitas": float(deficit.sum()),
        "horas_con_deficit": int((deficit > 0).sum()),
        "profesionales_por_hora": (a @ x).tolist(),
    }


def optimizar(demanda, horas, total_turnos):
    """Reparte `total_turnos` turnos de 8 h entre las 24 horas de inicio
    minimizando el déficit total de visitas (programación entera)."""
    t = len(demanda)
    a = matriz_cobertura()
    c = np.r_[np.zeros(24), np.ones(t)]
    m = np.zeros((t, 24 + t))
    for i in range(t):
        m[i, :24] = CAPACIDAD_POR_PROFESIONAL * a[horas[i]]
        m[i, 24 + i] = 1
    total = LinearConstraint(np.r_[np.ones(24), np.zeros(t)].reshape(1, -1), total_turnos, total_turnos)
    res = milp(
        c,
        constraints=[LinearConstraint(m, demanda, np.inf), total],
        integrality=np.r_[np.ones(24), np.zeros(t)],
        bounds=Bounds(0, np.inf),
    )
    x = np.round(res.x[:24]).astype(int)
    return {s: int(n) for s, n in enumerate(x) if n}


def main(ruta):
    df = pd.read_csv(ruta, parse_dates=["visit_start_datetime"])
    demanda = df["Predicted_Demand"].to_numpy(dtype=float)
    horas = df["visit_start_datetime"].dt.hour.to_numpy()
    total = sum(PLAN_FIJO.values())

    actual = evaluar(demanda, horas, PLAN_FIJO)
    propuesta_plan = optimizar(demanda, horas, total)
    propuesta = evaluar(demanda, horas, propuesta_plan)

    print(f"Personal total (turnos de 8 h): {total}")
    print(f"Plan fijo      -> cobertura {actual['cobertura']:.1%}, horas con déficit {actual['horas_con_deficit']}")
    print(f"Plan escalonado-> cobertura {propuesta['cobertura']:.1%}, horas con déficit {propuesta['horas_con_deficit']}")
    print("Inicios de turno propuestos (hora: profesionales):", propuesta_plan)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
