# Write your MySQL query statement below
SELECT USER_ID, MAX(TIME_STAMP) AS LAST_STAMP
FROM LOGINS
WHERE YEAR(TIME_STAMP) = 2020
GROUP BY USER_ID