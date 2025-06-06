SELECT 
    t.REG_ANS, 
    e.Nome_Fantasia, 
    MAX(t.DESCRICAO) AS DESCRICAO,  
    SUM(t.VL_SALDO_FINAL) AS total_despesas
FROM (
    SELECT `DATA`, REG_ANS, VL_SALDO_FINAL, DESCRICAO FROM `2024`
) t
JOIN tabela_empresas e ON t.REG_ANS = e.Registro_ANS
WHERE 
    t.DESCRICAO LIKE '%EVENTOS/SINISTROS INDENIZADOS DE ASSISTÊNCIA MÉDICO-HOSPITALAR%'
    AND t.`DATA` >= DATE_SUB(CURDATE(), INTERVAL 8 MONTH)
GROUP BY t.REG_ANS, e.Nome_Fantasia
ORDER BY total_despesas DESC
LIMIT 10;

SELECT DISTINCT `DATA` FROM `2024` ORDER BY `DATA` DESC;
