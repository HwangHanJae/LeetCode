# Write your MySQL query statement below
select customer_id, count(customer_id) as count_no_trans
from (
    select customer_id, Visits.visit_id, transaction_id
    from Visits
    left join Transactions
    on Visits.visit_id = Transactions.visit_id
    where transaction_id is null
) as t
group by customer_id