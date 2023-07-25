-- write a procedure to square a number.
-- Provide the number for squaring and fetch the result by using single parameter

DROP PROCEDURE IF EXISTS sp_square;
DELIMITER $$
CREATE PROCEDURE sp_square(INOUT p_n INT)
BEGIN
  SET p_n = p_n*p_n;
END;
$$
DELIMITER ;

-- SOURCE <path to your psm06.sql file>
-- SET @res = 8;
-- CALL sp_square(@res);
-- SELECT @res; 