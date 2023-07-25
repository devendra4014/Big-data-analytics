-- write a procedure to insert hello world into result table.

DROP PROCEDURE IF EXISTS sp_hello2;
DELIMITER $$
CREATE PROCEDURE sp_hello2()
BEGIN
    INSERT INTO result VALUES(1,"Hello World");
END;
$$
DELIMITER ;


-- SOURCE <path to your psm02.sql file>
-- CALL sp_hello2();