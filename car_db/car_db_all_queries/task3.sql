CREATE VIEW cars_with_models_and_brands AS 
SELECT car_id, brand_name, model_name, car_plate_num, rent_price
FROM car
INNER JOIN car_model USING(model_id)
INNER JOIN car_brand USING(brand_id);

SELECT * FROM cars_with_models_and_brands;

CREATE VIEW customer_addresses AS
SELECT name, surname, street, house, telephone_num
FROM customer
INNER JOIN address USING(address_id);

SELECT * FROM customer_addresses;

CREATE MATERIALIZED VIEW most_expensive_hondas AS
SELECT * FROM car
INNER JOIN car_model USING(model_id)
INNER JOIN car_brand USING(brand_id)
WHERE rent_price > 70::money and brand_name = 'Honda';

SELECT  * FROM most_expensive_hondas;
