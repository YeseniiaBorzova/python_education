CREATE DATABASE car_rent_db
WITH OWNER = postgres
ENCODING = 'UTF8';

CREATE TABLE city 
(
	city_id SERIAL PRIMARY KEY,
	city_name VARCHAR(50) NOT NULL
);

CREATE TABLE address 
(
	address_id SERIAL PRIMARY KEY,
	street VARCHAR(50) NULL,
	house SMALLINT NULL,
	telephone_num VARCHAR(30) NULL
);

CREATE TABLE car_brand 
(
	brand_id SERIAL PRIMARY KEY,
	brand_name VARCHAR(50) NOT NULL
);

CREATE TABLE car_model
(
	model_id SERIAL PRIMARY KEY,
	model_name VARCHAR(50) NOT NULL,
	brand_id INT NOT NULL,
	FOREIGN KEY (brand_id) REFERENCES car_brand(brand_id)
);

CREATE TABLE car
(
	car_id SERIAL PRIMARY KEY,
	rent_price money NOT NULL,
	car_plate_num VARCHAR(10) UNIQUE NOT NULL,
	model_id INT NOT NULL,
	FOREIGN KEY (model_id) REFERENCES car_model(model_id)
);

CREATE TABLE branch
(
	branch_id SERIAL PRIMARY KEY,
	branch_name VARCHAR(20) NOT NULL,
	address_id INT NOT NULL,
	city_id INT NOT NULL,
	FOREIGN KEY (address_id) REFERENCES address(address_id),
	FOREIGN KEY (city_id) REFERENCES city(city_id)
);

CREATE TABLE customer 
(
	customer_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	surname VARCHAR(30) NOT NULL,
	address_id INT NOT NULL,
	city_id INT NOT NULL,
	FOREIGN KEY (address_id) REFERENCES address(address_id),
	FOREIGN KEY (city_id) REFERENCES city(city_id)
);

CREATE TABLE rent 
(
	rent_id SERIAL PRIMARY KEY,
	customer_id INT NOT NULL,
	branch_id INT NOT NULL,
	car_id INT NOT NULL,
	date_of_renting_from DATE NOT NULL,
	date_of_renting_to DATE NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
	FOREIGN KEY (branch_id) REFERENCES branch(branch_id),
	FOREIGN KEY (car_id) REFERENCES car(car_id)
);

INSERT INTO car_brand VALUES 
(default, 'Honda'),
(default, 'Toyota'),
(default, 'BMW'),
(default, 'Volkswagen'),
(default, 'Audi'),
(default, 'Alfa Romeo'),
(default, 'Ford'),
(default, 'Haval');

INSERT INTO car_model VALUES 
(default, 'Civic Type R', 1),
(default, 'Civic SI', 1),
(default, 'Civic', 1),
(default, 'Accord', 1),
(default, 'CRZ', 1),
(default, 'Camry', 2),
(default, 'RAV4', 2),
(default, 'Highlander', 2),
(default, 'Corolla', 2),
(default, 'X5', 3),
(default, 'X6', 3),
(default, 'X4', 3),
(default, 'X3', 3),
(default, 'Series 2', 3),
(default, 'Series 3', 3),
(default, 'Series 4', 3),
(default, 'Series 5', 3),
(default, 'T-ROC', 4),
(default, 'Tiguan', 4),
(default, 'Passat', 4),
(default, 'Passat Arteon', 4),
(default, 'Golf', 4),
(default, 'Golf GTI', 4),
(default, 'Golf R', 4),
(default, 'Q3', 5),
(default, 'Q5', 5),
(default, 'Q8', 5),
(default, 'A5', 5),
(default, 'A6', 5),
(default, 'RS6', 5),
(default, 'Giulia', 6),
(default, 'Stelvio', 6),
(default, 'Giulietta', 6),
(default, 'Puma', 7),
(default, 'Mondeo', 7),
(default, 'Focus', 7),
(default, 'Focus ST', 7),
(default, 'Focus RS', 7),
(default, 'H2', 8),
(default, 'H4', 8),
(default, 'H6', 8),
(default, 'H9', 8);



CREATE SEQUENCE city_seq
INCREMENT 1
START 1;

CREATE SEQUENCE address_seq
INCREMENT 2
START 1;

CREATE SEQUENCE id_seq
INCREMENT 1
START 1;

CREATE SEQUENCE tel_num_seq AS BIGINT
INCREMENT 1
START 3807433666;

CREATE SEQUENCE cust_id_seq
INCREMENT 1
START 1;

CREATE SEQUENCE branch_id_seq
INCREMENT 1
START 1;

CREATE SEQUENCE car_id_seq
INCREMENT 1
START 1;

CREATE SEQUENCE car_num_seq
INCREMENT 11
START 1346;

CREATE SEQUENCE rent_id_seq
INCREMENT 1
START 1;

CREATE SEQUENCE customer_seq
INCREMENT 1
START 1
MAXVALUE 2500;

CREATE SEQUENCE car_seq
INCREMENT 1
START 1;




--inserting 20 cities
CREATE OR REPLACE PROCEDURE insert_cities( cities_amount int)
AS $$
DECLARE 
 	query text;
 	BEGIN
 	query := 'INSERT INTO city VALUES ';
 	FOR i IN 2..cities_amount LOOP
	query := query || ' (' || nextval('city_seq') || ',' || '''city ' || currval('city_seq') || '''),';
 		IF i = cities_amount THEN
 			query := query || ' (' || nextval('city_seq') || ',' || '''city ' || currval('city_seq') || ''');';
 		END IF;
 	END LOOP;
 	EXECUTE query;
 	END;
$$ LANGUAGE plpgsql
CALL insert_cities(20);

--inserting 2000 addresses
CREATE OR REPLACE PROCEDURE insert_addresses(id_amount int)
AS $$
DECLARE
	house_num int;
 	BEGIN
 	FOR i IN 1..id_amount LOOP
	house_num := floor(random()* (150-1 + 1) + 1);
 	INSERT INTO address VALUES (nextval('id_seq'), 'street ' || nextval('address_seq')::varchar, house_num, nextval('tel_num_seq')::varchar);
 	END LOOP;
 	END;
$$ LANGUAGE plpgsql
CALL insert_addresses(2000);

--inserting 5000 customers
CREATE OR REPLACE PROCEDURE insert_customers(customers_amount int)
AS $$
DECLARE
 	addres_id int;
 	city_id int;
  	BEGIN
 	FOR i IN 1..customers_amount LOOP
 	addres_id := floor(random()* (2000-1 + 1) + 1);
 	city_id := floor(random()* (20-1 + 1) + 1);
 	INSERT INTO customer VALUES (nextval('cust_id_seq'), 'name ' || currval('cust_id_seq')::varchar, 'surname ' || currval('cust_id_seq')::varchar, addres_id, city_id);
  	END LOOP;
  	END;
$$ LANGUAGE plpgsql
CALL insert_customers(5000);

--inserting 150 branches
CREATE OR REPLACE PROCEDURE insert_branches(branch_amount int)
AS $$
DECLARE
  	addres_id int;
  	city_id int;
   	BEGIN
  	FOR i IN 1..branch_amount LOOP
  	addres_id := floor(random()* (2000-1 + 1) + 1);
  	city_id := floor(random()* (20-1 + 1) + 1);
  	INSERT INTO branch VALUES (nextval('branch_id_seq'), 'branch ' || currval('branch_id_seq')::varchar, addres_id, city_id);
   	END LOOP;
   	END;
$$ LANGUAGE plpgsql
CALL insert_branches(150);

--inserting 3000 cars
CREATE OR REPLACE PROCEDURE insert_cars(car_amount int)
AS $$
DECLARE
  	model_id int;
  	rent_price int;
   	BEGIN
  	FOR i IN 1..car_amount LOOP
  	model_id := floor(random()* (42-1 + 1) + 1);
  	rent_price := floor(random()* (100-20 + 1) + 1);
  	INSERT INTO car VALUES (nextval('car_id_seq'), rent_price::money, '# ' || nextval('car_num_seq')::varchar, model_id);
   	END LOOP;
   	END;
$$ LANGUAGE plpgsql
CALL insert_cars(3000);

--inserting 2500 rents
CREATE OR REPLACE PROCEDURE insert_rents(rent_amount int)
AS $$
DECLARE
    	customer_id int;
    	branch_id int;
  	car_id int;
     	BEGIN
   	FOR i IN 1..rent_amount LOOP
   	branch_id := floor(random()* (150-1 + 1) + 1);
    	INSERT INTO rent(rent_id, customer_id, branch_id, car_id) VALUES (nextval('rent_id_seq'), nextval('customer_seq'), branch_id, nextval('car_seq'));
     	END LOOP;
    	END;
$$ LANGUAGE plpgsql
CALL insert_rents(2500);

--setting rent dates
UPDATE rent SET date_of_renting_from = NOW() - '1 days'::INTERVAL * ROUND(RANDOM() * 100) where rent_id between 1 and 2500
UPDATE rent SET date_of_renting_from = NOW() - '1 days'::INTERVAL * ROUND(RANDOM()
 * 20) where rent_id between 1 and 2500
 
--swapping dates where they are incorrect
UPDATE rent SET date_of_renting_from = date_of_renting_to, date_of_renting_to = date_of_renting_from where date_of_renting_to::date < date_of_renting_from::date

