CREATE VIEW products_view AS 
SELECT * FROM products;

DROP VIEW IF EXISTS products_view;

CREATE VIEW orders_with_statuses AS
SELECT * FROM orders
INNER JOIN order_status USING(order_status_id);

DROP VIEW IF EXISTS orders_with_statuses;

CREATE VIEW products_with_categories AS
SELECT * FROM products
INNER JOIN categories USING(category_id);

DROP VIEW IF EXISTS products_with_categories;

CREATE TABLE my_materialized_view AS SELECT 
users.first_name, users.last_name, users.city, carts.total, 
time_stamp, orders.created_at, orders.updated_at, 
SUM(carts.total) AS money_spent_on_all_orders
FROM carts
INNER JOIN users USING(user_id)
INNER JOIN orders USING(cart_id)
WHERE carts.total > 500::money
GROUP BY users.first_name, users.last_name, users.city, carts.total, 
time_stamp, orders.created_at, orders.updated_at
ORDER BY SUM(carts.total) DESC;

CREATE MATERIALIZED VIEW materialized_view AS SELECT * FROM my_materialized_view;

DROP MATERIALIZED VIEW IF EXISTS materialized_view;
