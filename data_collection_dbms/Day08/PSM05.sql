-- write a procedure to square a number.
-- Provide the number for squaring and fetch the result in an out parameter

DROP PROCEDURE IF EXISTS sp_square;
DELIMITER $$
CREATE PROCEDURE sp_square(IN p_n INT, OUT p_r INT)
BEGIN
  SET p_r = p_n*p_n;
END;
$$
DELIMITER ;

-- SOURCE <path to your psm05.sql file>
-- SELECT @res;
-- CALL sp_square(5, @res);
-- SELECT @res; 