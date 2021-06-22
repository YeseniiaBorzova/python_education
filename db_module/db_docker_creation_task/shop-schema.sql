CREATE DATABASE IF NOT EXIST shop;

CREATE TABLE users
(
user_id SERIAL PRIMARY KEY,
email VARCHAR(40) NOT NULL,
password VARCHAR(20) NOT NULL,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
middle_name VARCHAR(30) NOT NULL,
is_staff BOOLEAN NOT NULL,
country VARCHAR(20) NOT NULL,
city VARCHAR(30) NOT NULL,
addres TEXT NOT NULL
);

CREATE TABLE carts
(
cart_id SERIAL PRIMARY KEY,
user_id INT NOT NULL,
subtotal MONEY NOT NULL,
total MONEY NOT NULL,
time_stamp TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE order_status
(
order_status_id SERIAL PRIMARY KEY,
status_name VARCHAR(20) NOT NULL
);

CREATE TABLE orders
(
order_id SERIAL PRIMARY KEY,
cart_id INT NOT NULL,
order_status_id INT NOT NULL,
shipping_total DECIMAL NOT NULL,
total DECIMAL(2) NOT NULL,
created_at DATE NOT NULL,
updated_at DATE NOT NULL,
FOREIGN KEY (cart_id) REFERENCES carts (cart_id),
FOREIGN KEY (order_status_id) REFERENCES order_status (order_status_id)
);

CREATE TABLE categories
(
category_id SERIAL PRIMARY KEY,
category_title VARCAHR(30) NOT NULL,
category_description TEXT NOT NULL
);

CREATE TABLE products 
(
product_id SERIAL PRIMARY KEY,
product_title VARCHAR(20) NOT NULL,
prodcut_description TEXT NOT NULL,
in_stock BOOLEAN NOT NULL,
price MONEY NOT NULL,
slug VARCHAR(30) NOT NULL,
category_id INT NOT NULL,
FOREIGN KEY (category_id) REFERENCES categories (category_id)
);

CREATE TABLE cart_product
(
cart_id INT NOT NULL,
product_id INT NOT NULL,
FOREIGN KEY (cart_id) REFERENCES carts (cart_id),
FOREIGN KEY (product_id) REFERENCES products (product_id)
);
