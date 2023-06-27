# Write your MySQL query statement below
with Result as (select Prices.product_id, start_date, end_date, purchase_date, price, units
from Prices
join UnitsSold
on Prices.product_id = UnitsSold.product_id
where purchase_date between start_date and end_date)

select product_id, round(sum(price*units) / sum(units),2) as average_price
from Result
group by product_id
