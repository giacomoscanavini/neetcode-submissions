-- Write your query below
WITH ValueTable AS (
    SELECT 
        vl.value as left_value, 
        e.left_operand, 
        e.operator, 
        e.right_operand, 
        vr.value as right_value
    FROM Expressions e
    LEFT JOIN Variables vl ON e.left_operand = vl.name
    LEFT JOIN Variables vr ON e.right_operand = vr.name
)

SELECT vt.left_operand, vt.operator, vt.right_operand,
    CASE
        WHEN vt.operator = '>' THEN vt.left_value > vt.right_value 
        WHEN vt.operator = '<' THEN vt.left_value < vt.right_value 
        ELSE vt.left_value = vt.right_value 
    END AS value
FROM ValueTable vt
