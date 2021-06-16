CREATE TABLE potential_customer
( potent_customer_id SERIAL PRIMARY KEY,
 email VARCHAR(20) NOT NULL,
 name VARCHAR(20) NOT NULL,
 surname VARCHAR(20) NOT NULL,
 second_name VARCHAR(20) NOT NULL,
 city VARCHAR(30) NOT NULL
);

INSERT INTO potential_customer (email, name, surname, second_name, city) VALUES 
('email_1@gamil.com', 'name_1', 'surname_1', 'second_name_1', 'city 1'),
('email_2@gamil.com', 'name_2', 'surname_2', 'second_name_2', 'city 2'),
('email_3@gamil.com', 'name_3', 'surname_3', 'second_name_3', 'city 3'),
('email_4@gamil.com', 'name_4', 'surname_4', 'second_name_4', 'city 4'),
('email_5@gamil.com', 'name_5', 'surname_5', 'second_name_5', 'city 5'),
('email_7@gamil.com', 'name_7', 'surname_7', 'second_name_7', 'city 17'),
('email_8@gamil.com', 'name_8', 'surname_8', 'second_name_8', 'city 17'),
('email_9@gamil.com', 'name_9', 'surname_9', 'second_name_9', 'city 17'),
('email_10@gamil.com', 'name_10', 'surname_10', 'second_name_10', 'city 17');
--1
SELECT users.first_name, users.email
FROM users
WHERE city = 'city 17'
UNION
SELECT potential_customer.name, potential_customer.email 
FROM potential_customer
WHERE city = 'city 17';
--2
SELECT first_name, email 
FROM users
ORDER BY city, first_name ASC;
--3
SELECT category_title, COUNT(products.category_id) AS "amount_of_products"
FROM products
INNER JOIN categories
ON categories.category_id = products.category_id
GROUP BY category_title
ORDER BY COUNT(products.category_id) DESC;
--4.1
SELECT product_title 
FROM products
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM cart_product);
--4.2
SELECT product_title FROM products
WHERE product_id IN
(SELECT product_id FROM cart_product
WHERE cart_id IN
(SELECT carts.cart_id from carts
LEFT JOIN orders 
ON orders.cart_id = carts.cart_id
WHERE orders.cart_id is NULL))
--4.3
SELECT product_title, COUNT(cart_id) FROM products
INNER JOIN cart_product
ON cart_product.product_id = products.product_id
GROUP BY product_title
ORDER BY COUNT(cart_id) DESC
LIMIT 10;
--4.4
SELECT product_title, COUNT(orders.order_id) FROM carts
INNER JOIN orders
ON orders.cart_id = carts.cart_id
INNER JOIN cart_product
ON carts.cart_id = cart_product.cart_id
INNER JOIN products
ON products.product_id = cart_product.cart_id
WHERE order_status_id <> 5
GROUP BY product_title
ORDER BY COUNT(orders.order_id) DESC
LIMIT 10;
--4.5
SELECT SUM(total) AS "total_spend_money_on_orders", users.first_name, users.last_name FROM users
INNER JOIN carts USING(user_id)
GROUP BY user_id
ORDER BY COUNT(users.first_name) DESC
LIMIT 5;
--4.6
SELECT users.first_name, users.last_name, COUNT(carts.user_id) FROM users
INNER JOIN carts
ON users.user_id = carts.user_id
INNER JOIN orders
ON orders.cart_id = carts.cart_id
GROUP BY users.first_name, users.last_name
ORDER BY  COUNT(carts.user_id) DESC
LIMIT 5;
--4.7
SELECT first_name, last_name FROM users
WHERE user_id IN
(SELECT user_id FROM carts
LEFT JOIN orders USING(cart_id)
WHERE orders.cart_id is NULL)
LIMIT 5;
