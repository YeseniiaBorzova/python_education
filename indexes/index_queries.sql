EXPLAIN ANALYZE 
SELECT * FROM products 
WHERE product_title='Product 2000' OR product_title='Product 2500'
CREATE INDEX product_title_idx ON products (product_title);

EXPLAIN ANALYZE 
SELECT * FROM carts 
ORDER BY time_stamp;
CREATE INDEX carts_idx ON carts (time_stamp)

EXPLAIN ANALYZE SELECT * FROM carts
INNER JOIN users
ON users.user_id = carts.user_id
WHERE users.user_id = 10
ORDER BY users.last_name;
CREATE INDEX users_idx ON users (user_id, last_name);
CREATE INDEX carts_idx ON carts (user_id);

EXPLAIN ANALYZE SELECT * from products
INNER JOIN categories
ON products.category_id = categories.category_id
WHERE categories.category_id BETWEEN 1 AND 10
ORDER BY categories.category_id;
CREATE INDEX categories_idx ON categories(category_id)
CREATE INDEX products_idx ON products(category_id)
