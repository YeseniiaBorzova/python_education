2.1.1
SELECT * FROM users;
2.1.2
SELECT * FROM products;
2.1.3
SELECT * FROM order_status;
2.2
SELECT * FROM orders
WHERE order_status_id = 3 or order_status_id = 4
ORDER BY order_id ASC;
2.3.1
SELECT product_title, price FROM products
WHERE price > 80.0::money and price <= 150.0::money;
2.3.1
SELECT product_title, price FROM products
WHERE price BETWEEN 80.01::money and 150::money;
2.3.2
SELECT * FROM orders  
WHERE order_status_id = 4 and created_at::date > DATE'2020-10-01';
2.3.3
SELECT * FROM orders
WHERE created_at::date BETWEEN '2020-01-01'::date AND '2020-06-30'::date;
2.3.3
SELECT * FROM orders
WHERE created_at::date >= '2020-01-01'::date AND created_at::date <= '2020-06-30'::date;
2.3.4
SELECT product_title, category_id FROM products 
WHERE category_id = 7 OR category_id = 11 OR category_id = 18;
2.3.4
SELECT product_title, category_id FROM products 
WHERE category_id IN (7, 11, 18);
2.3.5
SELECT * FROM orders
WHERE order_status_id = 2 AND updated_at::date = '2020-12-31'::date;
2.3.6
SELECT * FROM carts
INNER JOIN orders
ON orders.cart_id = carts.cart_id
WHERE order_status_id = 5;

2.4.1
SELECT AVG(total::numeric)::money  AS avg_cost FROM carts
WHERE cart_id IN(SELECT cart_id FROM orders
WHERE order_status_id = 4);
2.4.2
SELECT MAX(total) AS max_cost FROM carts
WHERE time_stamp BETWEEN '2020-07-01' AND '2020-09-30';

