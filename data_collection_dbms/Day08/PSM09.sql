-- Write a trigger to modify the balance in accounts table on insert in transaction table

DROP TRIGGER IF EXISTS update_balance;
DELIMITER $$
CREATE TRIGGER update_balance
AFTER INSERT ON transactions
FOR EACH ROW
BEGIN
   IF NEW.tx_type = "credit" THEN
        UPDATE accounts SET balance = balance + NEW.amount WHERE accno = NEW.accno;
    ELSE
        UPDATE accounts SET balance = balance - NEW.amount WHERE accno = NEW.accno;
    END IF;
END;
$$
DELIMITER ;