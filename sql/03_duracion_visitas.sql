-- Duración promedio por tipo de visita (horas), excluyendo registros inválidos
SELECT
    c.concept_name AS tipo_visita,
    COUNT(*)       AS n_visitas,
    AVG(EXTRACT(EPOCH FROM (v.visit_end_datetime - v.visit_start_datetime)) / 3600) AS horas_promedio
FROM uninorte_omop.visit_occurrence v
JOIN uninorte_omop.concept c ON c.concept_id = v.visit_concept_id
WHERE v.visit_end_datetime >= v.visit_start_datetime
GROUP BY c.concept_name
ORDER BY n_visitas DESC;
