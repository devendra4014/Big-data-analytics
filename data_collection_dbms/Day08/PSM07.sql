-- write a procedure to find out whether a given number is even or odd

DROP PROCEDURE IF EXISTS sp_even_odd;
DELIMITER $$
CREATE PROCEDURE sp_even_odd(IN p_num INT)
BEGIN
    IF p_num%2=0 THEN
        SELECT "Given number is even" AS msg;
    ELSE
        SELECT "Given number is odd" AS msg;
    END IF;
END;
$$
DELIMITER ;

-- SOURCE <path to your psm07.sql file>
-- CALL sp_even_odd(6);
-- CALL sp_even_odd(3);