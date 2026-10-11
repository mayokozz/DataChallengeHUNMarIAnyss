-- Tamaño y rango de fechas (PostgreSQL)
SELECT
    COUNT(*)                  AS n_visitas,
    COUNT(DISTINCT person_id) AS n_pacientes,
    MIN(visit_start_datetime) AS primera_visita,
    MAX(visit_start_datetime) AS ultima_visita
FROM uninorte_omop.visit_occurrence;
