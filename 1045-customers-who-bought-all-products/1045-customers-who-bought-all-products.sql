# Write your MySQL query statement below

with Customer_de as (
select distinct(customer_id), product_key
from Customer
)


select customer_id
from (
    select customer_id, count(product_key) as key_count
    from Customer_de
    group by customer_id
    having key_count = (select count(product_key) as cnt from Product)
    ) as t
