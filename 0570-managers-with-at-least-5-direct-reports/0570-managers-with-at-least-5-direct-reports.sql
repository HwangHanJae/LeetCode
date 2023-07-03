# Write your MySQL query statement below
select mng.name as name
from Employee emp
join Employee mng
on emp.managerId = mng.id
group by mng.name
having count(mng.name) >= 5