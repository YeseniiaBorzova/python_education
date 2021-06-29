--insert car procedure
CREATE OR REPLACE PROCEDURE new_car_insert(car_id integer, rent_price numeric, car_plate_num varchar, model_id integer )
AS $$
   	BEGIN
		INSERT INTO car VALUES(car_id, rent_price::money, car_plate_num, model_id);
 			IF LEFT(car_plate_num, 1) = '#' THEN
 				IF rent_price > 0 THEN
   					COMMIT;
 				ELSE
 					ROLLBACK;
 			END IF;
   		ELSE
   			ROLLBACK;
  		END IF;
  	END;
$$ LANGUAGE plpgsql;
CALL new_car_insert(3002, -56.25, '#30012', 5);

--updating phone number
CREATE OR REPLACE PROCEDURE update_phone_number(id integer, phone_num varchar)
AS $$
    	BEGIN
	UPDATE address SET telephone_num = phone_num WHERE address_id = id;
  		IF LENGTH(phone_num) = 10 THEN	
    			COMMIT;
    		ELSE
    			ROLLBACK;
   		END IF;
   	END;
$$ LANGUAGE plpgsql;
CALL update_phone_number(1, '3806723')

