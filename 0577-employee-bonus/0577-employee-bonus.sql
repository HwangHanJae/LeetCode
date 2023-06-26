# Write your MySQL query statement below
with result as (select Employee.empId, name, supervisor, salary, bonus
from Employee
left join Bonus
on Employee.empId = Bonus.empId)

select name, bonus
from result
where bonus is null or bonus < 1000