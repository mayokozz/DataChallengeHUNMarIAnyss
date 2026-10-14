-- Tamaño y rango de fechas (PostgreSQL)
SELECT
    COUNT(*)                  AS n_visitas,
    COUNT(DISTINCT person_id) AS n_pacientes,
    MIN(visit_start_datetime) AS primera_visita,
    MAX(visit_start_datetime) AS ultima_visita
FROM uninorte_omop.visit_occurrence;
-- Cantidad de filas por tabla
SELECT 'person' AS tabla, COUNT(*) AS filas FROM uninorte_omop.person
UNION ALL SELECT 'visit_occurrence',      COUNT(*) FROM uninorte_omop.visit_occurrence
UNION ALL SELECT 'visit_detail',          COUNT(*) FROM uninorte_omop.visit_detail
UNION ALL SELECT 'condition_occurrence',  COUNT(*) FROM uninorte_omop.condition_occurrence
UNION ALL SELECT 'procedure_occurrence',  COUNT(*) FROM uninorte_omop.procedure_occurrence
UNION ALL SELECT 'measurement',           COUNT(*) FROM uninorte_omop.measurement
UNION ALL SELECT 'concept',               COUNT(*) FROM uninorte_omop.concept;
-- Periodo de los datos --
SELECT
    COUNT(*)                  AS n_visitas,
    COUNT(DISTINCT person_id) AS n_pacientes,
    MIN(visit_start_datetime) AS primera_visita,
    MAX(visit_start_datetime) AS ultima_visita
FROM uninorte_omop.visit_occurrence;
-- Tipos de visitas 
SELECT
    c.concept_name AS tipo_visita,
    COUNT(*)       AS n_visitas
FROM uninorte_omop.visit_occurrence v
JOIN uninorte_omop.concept c ON c.concept_id = v.visit_concept_id
GROUP BY c.concept_name
ORDER BY n_visitas DESC;

