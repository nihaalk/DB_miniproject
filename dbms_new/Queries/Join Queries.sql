--  All faculty members who are professors
SELECT
    faculty_id,
    faculty_name,
    designation,
    department_name
FROM
    faculty
NATURAL JOIN
    department
WHERE
    designation = 'professor';


