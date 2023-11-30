-- Teachers and their Tenure 
SELECT
    faculty_name AS Teacher_Name,
    dnumber AS Department_Number,
    YEAR(CURRENT_DATE) - joined AS Years_Working
FROM
    faculty;

--Hostels and no of students 
SELECT
hostel_name,
COUNT(*) AS Number_of_Students
FROM
rooms natural join hostel
GROUP BY
hostel_id;

-- No of students in each department 
SELECT
    department_name AS Department_Name,
    COUNT(*) AS Number_of_Students
FROM
    student natural join department
GROUP BY
    dnumber;


-- Find Faculty members who are not faculty advisors
SELECT
    f.faculty_id,
    f.faculty_name
FROM
    faculty f
LEFT JOIN
    fa ON f.faculty_id = fa.faculty_id
WHERE
    fa.faculty_id IS NULL;


