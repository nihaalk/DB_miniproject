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