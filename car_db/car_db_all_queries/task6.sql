--prohibit change rent trigger
CREATE FUNCTION rent_change_prohibit() RETURNS TRIGGER 
AS $$
BEGIN
 	IF NEW.rent_id <> OLD.rent_id THEN
  		RAISE EXCEPTION 'You can change only renting date!';
  	END IF;
	IF NEW.car_id <> OLD.car_id THEN
  		RAISE EXCEPTION 'You can change only renting date!';
  	END IF;
 	IF NEW.branch_id <> OLD.branch_id THEN
  		RAISE EXCEPTION 'You can change only renting date!';
  	END IF;
 	IF NEW.customer_id <> OLD.customer_id THEN
  		RAISE EXCEPTION 'You can change only renting date!';
  	END IF;
END;
$$ LANGUAGE plpgsql

CREATE TRIGGER rent_trigger AFTER UPDATE ON rent
FOR EACH ROW EXECUTE PROCEDURE rent_change_prohibit();

UPDATE rent SET car_id = 28 WHERE rent_id = 1;

--prohibit delete information from rent
CREATE FUNCTION rent_delete_prohibit() RETURNS TRIGGER 
AS $$
BEGIN
   	IF (TG_OP = 'DELETE') THEN
			RAISE EXCEPTION 'You cant delete any information from rent table';
    	END IF;
END;
$$ LANGUAGE plpgsql

CREATE TRIGGER rent_trigger BEFORE DELETE ON rent
FOR EACH ROW EXECUTE PROCEDURE rent_delete_prohibit();

UPDATE rent SET car_id = 28 WHERE rent_id = 1;

DELETE FROM rent WHERE rent_id = 2500;
