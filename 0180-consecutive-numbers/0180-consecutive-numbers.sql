# Write your MySQL query statement below
select Distinct(num) as ConsecutiveNums
from (
    select num,
            Lag(num, 1) over (order by id) As 'num2',
            Lag(num, 2) over (order by id) As 'num3'
    from Logs) as result
where result.num = result.num2 and result.num2 = result.num3
