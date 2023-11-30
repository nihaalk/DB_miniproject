
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

