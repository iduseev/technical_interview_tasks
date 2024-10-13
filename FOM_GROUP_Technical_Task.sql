SELECT product_id
FROM products
LEFT JOIN sales
ON products.product_id = sales.product_id
WHERE sale_id IS NULL;

SELECT *
FROM products
WHERE product_id not in (
    SELECT product_id
    FROM sales
    );