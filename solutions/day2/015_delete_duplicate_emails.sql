"""
196 Delete Duplicate Emails
https://leetcode.com/problems/delete-duplicate-emails/

Write a SQL query to delete all duplicate email entries in a table named Person, 
keeping only unique emails based on its smallest Id.
"""

DELETE p1 FROM Person p1
INNER JOIN Person p2 
WHERE 
    p1.Email = p2.Email AND
    p1.Id > p2.Id;