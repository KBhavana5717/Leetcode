# Write your MySQL query statement
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders);