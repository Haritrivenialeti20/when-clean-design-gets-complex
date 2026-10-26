from pathlib import Path
import sqlite3

root = Path(__file__).resolve().parents[1]
conn = sqlite3.connect(':memory:')
conn.execute('PRAGMA foreign_keys = ON')
conn.executescript((root / 'schema/normalized_schema.sql').read_text())
conn.executescript('''
INSERT INTO suppliers VALUES (1, 'Nova Supply', '555-0100', 'ops@nova.example');
INSERT INTO suppliers VALUES (2, 'DeskWorks', '555-0101', 'hello@deskworks.example');
INSERT INTO products VALUES (1, 'Pocket Phone', 299.00, 1);
INSERT INTO products VALUES (2, 'Mechanical Keyboard', 89.00, 2);
INSERT INTO categories VALUES (1, 'Electronics');
INSERT INTO categories VALUES (2, 'Accessories');
INSERT INTO product_categories VALUES (1, 1);
INSERT INTO product_categories VALUES (2, 2);
INSERT INTO tags VALUES (1, 'mobile');
INSERT INTO tags VALUES (2, 'office');
INSERT INTO product_tags VALUES (1, 1);
INSERT INTO product_tags VALUES (2, 2);
INSERT INTO warehouses VALUES (1, 'North Hub');
INSERT INTO warehouses VALUES (2, 'South Hub');
INSERT INTO inventory VALUES (1, 1, 4);
INSERT INTO inventory VALUES (2, 1, 18);
INSERT INTO inventory VALUES (2, 2, 7);
''')

queries = [
    ('all products', '''SELECT p.product_id, p.product_name, p.price, s.supplier_name, s.supplier_email FROM products p JOIN suppliers s ON s.supplier_id = p.supplier_id ORDER BY p.product_id'''),
    ('electronics', '''SELECT p.product_id, p.product_name, p.price FROM products p JOIN product_categories pc ON pc.product_id = p.product_id JOIN categories c ON c.category_id = pc.category_id WHERE c.category_name = 'Electronics' ORDER BY p.product_name'''),
    ('supplier details', '''SELECT p.product_name, s.supplier_name, s.supplier_phone, s.supplier_email FROM products p JOIN suppliers s ON s.supplier_id = p.supplier_id ORDER BY p.product_name'''),
    ('low stock', '''SELECT p.product_name, w.warehouse_location, i.stock_quantity FROM products p JOIN inventory i ON i.product_id = p.product_id JOIN warehouses w ON w.warehouse_id = i.warehouse_id WHERE i.stock_quantity < 10 ORDER BY i.stock_quantity ASC, p.product_name'''),
    ('mobile tag', '''SELECT p.product_name, t.tag_name FROM products p JOIN product_tags pt ON pt.product_id = p.product_id JOIN tags t ON t.tag_id = pt.tag_id WHERE t.tag_name = 'mobile' ORDER BY p.product_name'''),
]

for name, sql in queries:
    rows = conn.execute(sql).fetchall()
    assert rows, f'{name} query returned no rows'
    print(f'{name}: {len(rows)} row(s)')

assert conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'").fetchone()[0] == 8
assert conn.execute("SELECT product_name FROM products WHERE product_id = 1").fetchone()[0] == 'Pocket Phone'
print('verification passed: schema loads, foreign keys enabled, and all 5 normalized queries return data')
