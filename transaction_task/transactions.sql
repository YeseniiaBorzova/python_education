BEGIN;
SAVEPOINT before_update;
UPDATE categories SET category_title = 'CATEGORY 1' WHERE category_id = 1;
ROLLBACK TO before_update;

BEGIN;
UPDATE users SET first_name = 'FIRST_NAME1' WHERE user_id = 1;
SAVEPOINT before_cart_delete;
DELETE FROM cart_product where cart_id = 1 AND product_id = 3943;
ROLLBACK TO before_cart_delete;
COMMIT;

BEGIN;
INSERT INTO categories VALUES (21, 'Category 21', 'Category 21 description');
UPDATE products SET slug = 'PRODUCT-1' WHERE product_id = 1;
DELETE FROM cart_product WHERE cart_id = 1;
ROLLBACK;

BEGIN;
SAVEPOINT before_delete;
DELETE FROM orders WHERE order_id = 5;
SAVEPOINT before_insert;
INSERT INTO order_status VALUES (6, 'Delivered');
SAVEPOINT before_update;
UPDATE users SET email = 'ITFIYTFIYFIi@leurh' WHERE user_id = 1;
ROLLBACK TO before_insert;
ROLLBACK TO before_delete;
COMMIT;

BEGIN;
DELETE FROM cart_product WHERE cart_id = 2;
DELETE FROM orders WHERE order_id = 3;
UPDATE carts SET total = 333.33 WHERE cart_id = 2;
INSERT INTO cart_product VALUES (4, 22), (4, 25), (4, 51);
ROLLBACK;
