-- NORMALIZED PRODUCT QUERIES
-- These queries intentionally use JOINs because relationships now live in dedicated tables.

-- Query 1: Get all products with their supplier.
SELECT
    p.product_id,
    p.product_name,
    p.price,
    s.supplier_name,
    s.supplier_email
FROM products AS p
JOIN suppliers AS s ON s.supplier_id = p.supplier_id
ORDER BY p.product_id;

-- Query 2: Find products in a specific category.
SELECT
    p.product_id,
    p.product_name,
    p.price
FROM products AS p
JOIN product_categories AS pc ON pc.product_id = p.product_id
JOIN categories AS c ON c.category_id = pc.category_id
WHERE c.category_name = 'Electronics'
ORDER BY p.product_name;

-- Query 3: Find supplier details for a product.
SELECT
    p.product_name,
    s.supplier_name,
    s.supplier_phone,
    s.supplier_email
FROM products AS p
JOIN suppliers AS s ON s.supplier_id = p.supplier_id
ORDER BY p.product_name;

-- Query 4: Find products with low stock across warehouses.
SELECT
    p.product_name,
    w.warehouse_location,
    i.stock_quantity
FROM products AS p
JOIN inventory AS i ON i.product_id = p.product_id
JOIN warehouses AS w ON w.warehouse_id = i.warehouse_id
WHERE i.stock_quantity < 10
ORDER BY i.stock_quantity ASC, p.product_name;

-- Query 5: Optional normalized tag lookup, replacing a comma-separated tag search.
SELECT
    p.product_name,
    t.tag_name
FROM products AS p
JOIN product_tags AS pt ON pt.product_id = p.product_id
JOIN tags AS t ON t.tag_id = pt.tag_id
WHERE t.tag_name = 'mobile'
ORDER BY p.product_name;
