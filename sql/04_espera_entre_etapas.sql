-- Duración de cada etapa y espera entre etapas, por área
WITH pasos AS (
    SELECT
        visit_occurrence_id,
        visit_detail_concept_id,
        visit_detail_start_datetime AS inicio,
        visit_detail_end_datetime   AS fin,
        LAG(visit_detail_end_datetime) OVER (
            PARTITION BY visit_occurrence_id
            ORDER BY visit_detail_start_datetime
        ) AS fin_paso_anterior
    FROM uninorte_omop.visit_detail
    WHERE visit_detail_end_datetime >= visit_detail_start_datetime
)
SELECT
    c.concept_name AS area,
    COUNT(*)       AS n_pasos,
    AVG(EXTRACT(EPOCH FROM (p.fin - p.inicio)) / 60)               AS duracion_promedio_min,
    AVG(EXTRACT(EPOCH FROM (p.inicio - p.fin_paso_anterior)) / 60) AS espera_promedio_min
FROM pasos p
JOIN uninorte_omop.concept c ON c.concept_id = p.visit_detail_concept_id
GROUP BY c.concept_name
ORDER BY duracion_promedio_min DESC;
