-- write a procedure to calculate area of rectangle and insert it into result table
-- give the length and breadth from user.

DROP PROCEDURE IF EXISTS sp_rectangle_area;
DELIMITER $$
CREATE PROCEDURE sp_rectangle_area(IN p_len INT,IN p_bre INT)
BEGIN
  DECLARE area INT;
  SET area = p_len*p_bre;
  INSERT INTO result VALUES(area,CONCAT(p_len,"*",p_bre));  
END;
$$
DELIMITER ;

-- SOURCE <path to your psm04.sql file>
-- CALL sp_rectangle_area(10,5);