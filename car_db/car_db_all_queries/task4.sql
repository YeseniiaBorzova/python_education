--function with loop returns table
CREATE OR REPLACE FUNCTION get_n_cars(n int) RETURNS TABLE 
(car_id integer, rent_price money, car_plate_num varchar, model_name varchar, brand_name varchar)
 AS $$
BEGIN
 	FOR i IN 1..n LOOP
  	RETURN QUERY
 	SELECT car.car_id, car.rent_price, car.car_plate_num, car_model.model_name, car_brand.brand_name
  	FROM car
  	INNER JOIN car_model USING(model_id)
 	INNER JOIN car_brand USING(brand_id)
 	WHERE car.car_id = i;
	END LOOP;
END;
$$ LANGUAGE plpgsql;
SELECT get_n_cars(20);

--function with loop and cursor
CREATE OR REPLACE FUNCTION get_simular_surnames(pattern varchar) RETURNS SETOF varchar
AS $$
DECLARE
 	row  RECORD;
	surname_cursor CURSOR FOR SELECT surname FROM customer WHERE surname LIKE pattern;
BEGIN
  	OPEN surname_cursor;
 	  	LOOP
     		FETCH FROM surname_cursor INTO row;
     		EXIT WHEN NOT FOUND;
     		return next row;
   		END LOOP;
	CLOSE surname_cursor;
END;
$$ LANGUAGE plpgsql;

SELECT  get_simular_surnames('%e 1%');

