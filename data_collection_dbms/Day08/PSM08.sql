-- write a procedure to sum all the even numbers in the given range

DROP PROCEDURE IF EXISTS sp_sum_even;
DELIMITER $$
CREATE PROCEDURE sp_sum_even(IN p_low INT,IN p_high INT)
BEGIN
    DECLARE sum INT DEFAULT 0;
    WHILE p_low<=p_high DO
        IF p_low%2 = 0 THEN
            SET sum = sum+p_low;
        END IF;
        SET p_low = p_low + 1;
    END WHILE;
    SELECT "sum of even nos = " AS msg,sum;
END;
$$
DELIMITER ;

-- SOURCE <path to your psm08.sql file>
-- sp_sum_even(10,30);

    -- sum=0,v_low,v_high
    -- while(v_low<=v_high){
    --     if(v_low%2==0)
    --         sum = sum+v_low;
    --     v_low = v_low + 1;
    -- }
    -- print(sum)