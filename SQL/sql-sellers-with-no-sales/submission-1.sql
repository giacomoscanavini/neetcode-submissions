-- Write your query below
SELECT DISTINCT s.seller_name
FROM Seller s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.seller_id = s.seller_id
        AND EXTRACT(YEAR FROM o.sale_date) = 2020
)
ORDER BY s.seller_name ASC