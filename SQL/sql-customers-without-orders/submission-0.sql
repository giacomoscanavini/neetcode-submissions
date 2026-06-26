-- Write your query below
SELECT name
FROM Customers
WHERE name NOT IN (
    SELECT DISTINCT Customers.name
    FROM Orders
    LEFT JOIN Customers
        ON Orders.customer_id = Customers.id
)