--select with indexes
EXPLAIN ANALYZE 
SELECT * FROM car 
INNER JOIN car_model USING(model_id) 
INNER JOIN car_brand USING(brand_id)
GROUP BY brand_name, car_model.brand_id, car.model_id, car.car_id, car_model.model_name

CREATE INDEX brand_name ON car_brand (brand_name)
CREATE INDEX car_model_id ON car_model (brand_id, model_name);
CREATE INDEX car_id_idx ON car (model_id, car_id);

EXPLAIN ANALYZE 
SELECT * FROM customer 
INNER JOIN address USING (address_id) 
WHERE surname = 'surname 1' or surname = 'surname 111'

CREATE INDEX surname_idx ON customer (surname)


EXPLAIN ANALYZE 
SELECT * FROM customer 
INNER JOIN address USING(address_id) 
INNER JOIN city USING(city_id) 
ORDER BY house

CREATE INDEX house_idx ON address (house)
CREATE INDEX customer_idx ON customer (customer_id);
CREATE INDEX address_id_idx ON address (address_id);
CREATE INDEX city_idx ON city (city_id);

