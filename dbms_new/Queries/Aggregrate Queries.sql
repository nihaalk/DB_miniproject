-- to get number of drug instances associated with a case
select NameOfCase, count(*) from (DRUGS NATURAL JOIN CASES) group by CaseID;

-- Teachers with greater than average salary for their departmen
SELECT faculty_name
FROM faculty f
WHERE salary > (SELECT AVG(salary) FROM faculty WHERE dnumber = f.dnumber);


