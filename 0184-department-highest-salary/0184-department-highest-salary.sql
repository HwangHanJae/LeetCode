# Write your MySQL query statement below
SELECT HIGH.DEPARTMENT,
       EMPLOYEE.NAME AS EMPLOYEE,
       EMPLOYEE.SALARY
FROM (SELECT DEPARTMENTID, MAX(SALARY) AS MAX_SALARY, DEPARTMENT.NAME AS DEPARTMENT
FROM EMPLOYEE
JOIN DEPARTMENT
ON DEPARTMENT.ID = EMPLOYEE.DEPARTMENTID
GROUP BY DEPARTMENTID) HIGH
JOIN EMPLOYEE
ON EMPLOYEE.SALARY = HIGH.MAX_SALARY AND EMPLOYEE.DEPARTMENTID = HIGH.DEPARTMENTID