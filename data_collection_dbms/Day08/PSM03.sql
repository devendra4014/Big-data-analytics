-- Write a procedure to calculate area of circle
-- display the radius and area of circle on console

DROP PROCEDURE IF EXISTS sp_circle_area;
DELIMITER $$
CREATE PROCEDURE sp_circle_area()
BEGIN
    DECLARE radius INT DEFAULT 10;
    DECLARE area DOUBLE;
    SET area = 3.14 * radius * radius;
    SELECT radius ,area;
END;
$$
DELIMITER ;

-- SOURCE <path to your psm03.sql file>
-- CALL sp_circle_area();