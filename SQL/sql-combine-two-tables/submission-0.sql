-- Write your query below
SELECT Person.first_name, Person.last_name, Address.city, Address.state
FROM Person
LEFT JOIN Address
    ON Person.person_id = Address.person_id