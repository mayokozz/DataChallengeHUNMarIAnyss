-- Errores de registro en visitas
SELECT
    COUNT(*) FILTER (WHERE visit_end_datetime IS NULL)                AS sin_fin,
    COUNT(*) FILTER (WHERE visit_end_datetime < visit_start_datetime) AS fin_antes_de_inicio
FROM uninorte_omop.visit_occurrence;

-- Errores de registro en etapas (visit_detail)
SELECT
    COUNT(*) FILTER (WHERE visit_detail_end_datetime IS NULL)                       AS sin_fin,
    COUNT(*) FILTER (WHERE visit_detail_end_datetime < visit_detail_start_datetime) AS fin_antes_de_inicio
FROM uninorte_omop.visit_detail;
