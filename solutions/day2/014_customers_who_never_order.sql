"""
183 Customers Who Never Order
https://leetcode.com/problems/customers-who-never-order/

Write a SQL query to find all customers who never order anything.
"""

SELECT Name AS Customers
FROM Customers
WHERE Id NOT IN (SELECT CustomerId FROM Orders);