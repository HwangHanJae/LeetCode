# Write your MySQL query statement below
select product_name, sum(unit) as unit
from Products
join Orders
on Products.product_id = Orders.product_id
where date_format(order_date, '%Y-%m') = '2020-02'
group by product_name
having sum(unit) >= 100
