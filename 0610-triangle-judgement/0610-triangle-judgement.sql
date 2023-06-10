# Write your MySQL query statement below
select x,y,z,if(x < y+z and y < x+z and z < x+y, 'Yes', 'No') as triangle
from Triangle