-- Case Data
CREATE TABLE CASES(CaseID varchar(255) NOT NULL UNIQUE, TypeOfCase varchar(255),NameOfCase varchar(255), LeadingOfficer varchar(255), AsstOfficer varchar(255), TimeOfReport datetime NOT NULL, Loc varchar(255), statusOfCase varchar(255), PRIMARY KEY(CaseID));

-- Criminal Data
CREATE TABLE CRIMINAL(CID varchar(255) NOT NULL UNIQUE, CName varchar(255) NOT NULL, Alias varchar(255), Age int, NoOfCases int, DominantHand varchar(255), CurrentStatus varchar(255), DNAID varchar(50), FingerprintID varchar(50), nationality varchar(255), PRIMARY KEY(CID));

-- Criminal Case
CREATE TABLE CriminalCase(CriminalID varchar(255), CrimeID varchar(255), FOREIGN KEY(CriminalID) REFERENCES CRIMINAL(CID), FOREIGN KEY(CrimeID) REFERENCES CASES(CaseID));

-- Ballistics Data
CREATE TABLE BALLISTICS(CaseID varchar(255), B_ID varchar(255) NOT NULL UNIQUE,Model varchar(255), Manufacturer varchar(255), Year int, typeOfGun varchar(255), gauge float, caliber int, CountryOfOrigin varchar(255),PRIMARY KEY(B_ID), FOREIGN KEY(CaseID) REFERENCES CASES(CaseID) );

-- Drugs Data
CREATE TABLE DRUGS(CaseID varchar(255), NDC_No varchar(255) NOT NULL UNIQUE, dname varchar(255), color varchar(255), class varchar(255), narcotic varchar(255), PRIMARY KEY(NDC_No), FOREIGN KEY(CaseID) REFERENCES CASES(CaseID));

-- Paint Data
CREATE TABLE PAINT(CaseID varchar(255), PID varchar(255) NOT NULL UNIQUE, Color varchar(255) NOT NULL, Solvent varchar(255), Binder varchar(255), Pigments varchar(255), Additive varchar(255), PRIMARY KEY(PID), FOREIGN KEY(CaseID) REFERENCES CASES(CaseID));


-- Automobile Data
CREATE TABLE AUTOMOBILE(CaseID varchar(255), AID varchar(255), model varchar(255), Year int, Manufacturer varchar(255), typeOfVehicle varchar(255), PRIMARY KEY(AID), FOREIGN KEY(CaseID) REFERENCES CASES(CaseID));

-- 	Students SGPA
DELIMITER //
CREATE FUNCTION calculate_sgpa(student_id_input VARCHAR(20))
RETURNS DECIMAL(5, 2)
DETERMINISTIC
BEGIN
    DECLARE total_points DECIMAL(5, 2);
    DECLARE total_credits INT;
    
    SELECT
        SUM(marks * number_of_credits) INTO total_points
    FROM
        registered
        NATURAL JOIN course
    WHERE
        student_id = student_id_input;

    SELECT
        SUM(number_of_credits) INTO total_credits
    FROM
        registered
        NATURAL JOIN course
    WHERE
        student_id = student_id_input;

    IF total_credits > 0 THEN
        RETURN total_points / total_credits;
    ELSE
        RETURN NULL;
    END IF;
END //
DELIMITER ;

-- 	Bus Revenue
DELIMITER //
CREATE FUNCTION calculate_bus_revenue(b_id_input VARCHAR(20))
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
	DECLARE total_distance DECIMAL(10, 2);
	DECLARE revenue DECIMAL(10, 2);

	-- Calculate total distance for the given bus
	SELECT
	SUM(distance) INTO total_distance
	FROM
	bus_student_distance
	WHERE
	b_id = b_id_input;
	-- Calculate revenue using the provided formula
	SELECT
	cost_per_km * total_distance * 150 * 2 INTO revenue
	FROM
	WHERE
	b_id = b_id_input;
	RETURN revenue;
	END //

DELIMITER ;


DELIMITER //
CREATE TRIGGER check_sem_consistency_trigger
BEFORE INSERT ON teaches
FOR EACH ROW
BEGIN
    DECLARE faculty_sem INT;
    DECLARE course_sem INT;

    -- Get the semester for the faculty_id from the faculty table
    SELECT sem INTO faculty_sem
    FROM faculty
    WHERE faculty_id = NEW.faculty_id;

    -- Get the semester for the course_number from the course table
    SELECT sem INTO course_sem
    FROM course
    WHERE course_number = NEW.course_number;

    -- Check if the semesters are consistent, if not, delete the entry
    IF faculty_sem IS NOT NULL AND course_sem IS NOT NULL AND faculty_sem != course_sem THEN
        DELETE FROM teaches
        WHERE faculty_id = NEW.faculty_id AND course_number = NEW.course_number;
    END IF;
END;
//
DELIMITER ;

-- Create a trigger to enforce marks and department/semester consistency
DELIMITER //
CREATE TRIGGER check_grade_and_sem_consistency
    BEFORE INSERT ON registered
    FOR EACH ROW
    BEGIN
        DECLARE student_dnumber INT;
        DECLARE student_sem INT;
        DECLARE course_dnumber INT;
        DECLARE course_sem INT;
    
    -- Get the department number and semester for the student_id from the student table
        SELECT dnumber, sem INTO student_dnumber, student_sem
        FROM student
        WHERE student_id = NEW.student_id;
   
    -- Get the department number and semester for the course_number from the course table
        SELECT dnumber, sem INTO course_dnumber, course_sem
        FROM course
        WHERE course_number = NEW.course_number;
    
     -- Check if marks are in the range of 0 to 10 and department/semester consistency
        IF NEW.marks < 0 OR NEW.marks > 10 OR student_dnumber IS NULL OR student_sem IS NULL OR course_dnumber IS NULL OR course_sem IS NULL OR (student_dnumber, student_sem) != (course_dnumber, course_sem) THEN
             SIGNAL SQLSTATE '45000'
             SET MESSAGE_TEXT = 'Invalid input: Marks should be in the range of 0 to 100, and student department/semester should match course department/semester.';
        END IF;
    END;
    //

