--1
CREATE OR REPLACE FUNCTION set_shipping_total(city_name VARCHAR) 
RETURNS void
AS $$
DECLARE
  found_user int;
  found_cart int;
BEGIN
  SELECT user_id 
  INTO found_user
  FROM users 
  WHERE city = city_name;
  IF found_user is not NULL THEN
  	SELECT cart_id
	INTO found_cart
	FROM carts
	WHERE user_id = found_user;
		IF found_cart is not NULL THEN
  			UPDATE orders SET shipping_total = 0 WHERE cart_id = found_cart;
		ELSE
			RAISE NOTICE'Cart % id not found', found_cart;
		END IF;	
  END IF;
  IF NOT found THEN
  	RAISE NOTICE'User with % id not found', found_user;
  END IF;
END;
$$ LANGUAGE plpgsql;

SELECT set_shipping_total('city 3');


--2.1
CREATE OR REPLACE PROCEDURE transaction_test(category_id integer, category_title varchar, category_description text )
 AS $$
 	BEGIN
		INSERT INTO categories VALUES(category_id, category_title, category_description);
 		IF category_id > 1 THEN
 			COMMIT;
 		ELSE
 			ROLLBACK;
 		END IF;
	END;
$$ LANGUAGE plpgsql;

CALL transaction_test(21, 'Category 21', 'Category 21 description.');


--2.2
 CREATE OR REPLACE PROCEDURE inser_cart_product_test(start_product_id int, end_product_id int, start_cart_id int, end_cart_id int)
    AS $$
    	DECLARE 
 	query text;
    	BEGIN
 	query := 'INSERT INTO cart_product VALUES';
  		FOR i IN start_product_id..end_product_id LOOP
  			FOR j IN start_cart_id..end_cart_id LOOP
			query := query || ' (' || i || ',' || j ||'),';
				IF i = end_product_id AND j = end_cart_id THEN
					query := query || ' (' || i || ',' || j ||');';
				END IF;
  			END LOOP;
  		END LOOP;
 		EXECUTE query;
   	END;
$$ LANGUAGE plpgsql;
CALL inser_cart_product_test(1, 3, 55, 60);

--3
CREATE OR REPLACE FUNCTION get_product_and_categories() RETURNS TABLE 
(avg_price_by_category money, price money, product_title varchar, category_title varchar)
AS $$
BEGIN
 	RETURN QUERY
	SELECT AVG(products.price::numeric) OVER (PARTITION BY products.category_id)::money AS avg_price_by_category, 
 	products.price, products.product_title, categories.category_title
 	FROM products
 	INNER JOIN categories USING(category_id);	
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_product_and_categories();

--4.1
CREATE OR REPLACE FUNCTION product_trigger() RETURNS TRIGGER
AS $$
BEGIN
 	IF NEW.product_title IS NULL THEN
 		RAISE EXCEPTION 'Product title cannot be empty';
 	END IF;
 	IF NEW.price IS NULL THEN
 		RAISE EXCEPTION 'Product price cannot be empty';
 	END IF;
 	IF NEW.price < 0.01::money THEN
 		RAISE EXCEPTION 'Product cannot be free or have negative price';
	END IF;	
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER prod_trigger BEFORE INSERT OR UPDATE ON products
FOR EACH ROW EXECUTE PROCEDURE product_trigger();

--4.2
CREATE OR REPLACE FUNCTION order_date_change() RETURNS TRIGGER
AS $$
BEGIN
 	IF NEW.updated_at::date < OLD.updated_at::date THEN
 		RAISE EXCEPTION 'New order update date cannot be earlier than old order update date';
 	END IF;
 	IF NEW.created_at::date <> OLD.created_at::date THEN
 		RAISE EXCEPTION 'Order creation date cannot be changed';
 	END IF;
 	IF NEW.updated_at::date < OLD.created_at::date THEN
 		RAISE EXCEPTION 'Order update date cannot be earlier than order creation date';
	END IF;	
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER date_update AFTER UPDATE  OR INSERT ON orders
FOR EACH ROW EXECUTE PROCEDURE order_date_change();

