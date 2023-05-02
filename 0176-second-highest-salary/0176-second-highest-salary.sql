# Write your MySQL query statement below
SELECT 
  LEAD(salary) over(order by salary desc) as SecondHighestSalary
FROM Employee
group by salary
order by salary desc
Limit 1;
