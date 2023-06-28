# Write your MySQL query statement below

select teacher_id, sum(cnt) as cnt
from(
    select teacher_id, count(distinct(subject_id)) as cnt
    from Teacher
    group by teacher_id, subject_id) as t
group by teacher_id