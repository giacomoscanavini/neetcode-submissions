-- Write your query below
WITH 
    Customers_A AS (
        SELECT DISTINCT customer_id
        FROM Orders 
        WHERE product_name = 'A'
    ),
    Customers_B AS (
        SELECT DISTINCT customer_id
        FROM Orders 
        WHERE product_name = 'B'
    ),
    Customers_C AS (
        SELECT DISTINCT customer_id
        FROM Orders 
        WHERE product_name = 'C'
    )

SELECT DISTINCT k.customer_id, k.customer_name
FROM Customers k
INNER JOIN Customers_A a ON k.customer_id = a.customer_id
INNER JOIN Customers_B b ON k.customer_id = b.customer_id
WHERE k.customer_id NOT IN (
    SELECT customer_id
    FROM Customers_C
)
ORDER BY k.customer_name ASC