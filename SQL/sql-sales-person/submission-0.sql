-- Write your query below
WITH Orders_Crimson AS (
    SELECT o.sales_id
    FROM Orders o 
    LEFT JOIN Company c 
        ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
)

SELECT DISTINCT s.name
FROM Sales_person s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders_Crimson o
    WHERE o.sales_id = s.sales_id
)
ORDER BY s.name ASC