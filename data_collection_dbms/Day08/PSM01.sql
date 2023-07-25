-- write a procedure to display hello world as message

DROP PROCEDURE IF EXISTS sp_hello;
DELIMITER $$
CREATE PROCEDURE sp_hello()
BEGIN
    SELECT "Hello World" AS msg;
END;
$$
DELIMITER ;

-- SOURCE <path to your psm01.sql file>
-- CALL sp_hello();
