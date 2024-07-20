# Write your MySQL query statement below

SELECT Users.name as NAME, sum(Transactions.amount) as BALANCE FROM Users JOIN Transactions ON Users.account = Transactions.account GROUP BY Users.account HAVING sum(Transactions.amount) > 10000;
