-- Write your query below
WITH Travelled AS (
    SELECT u.name, SUM(r.distance) AS travelled_distance
    FROM Rides r
    LEFT JOIN Users u
        ON r.user_id = u.id
    GROUP BY u.name
)

SELECT u.name, COALESCE(t.travelled_distance, 0) AS travelled_distance
FROM Users u
LEFT JOIN Travelled t
    ON u.name = t.name
ORDER BY travelled_distance DESC, u.name ASC