# Normalization Review

## Findings in the original schema

The original `products` table violates First Normal Form because `categories` and `product_tags` contain comma-separated lists. Supplier name, phone, and email are repeated for every product supplied by the same company, creating update anomalies and a transitive dependency from `product_id` through `supplier_name` to the supplier attributes. Warehouse location and stock quantity are mixed into the product entity, which prevents one product from having independent inventory rows per warehouse.

## 3NF redesign

`products` now stores only product attributes and a `supplier_id` foreign key. Supplier attributes live in `suppliers`, while categories and tags are entities linked through `product_categories` and `product_tags`. `warehouses` and `inventory` separate stock facts from product identity; the inventory composite key permits one product in multiple warehouses without duplication.

Every table has a key, relationship tables have composite keys, and foreign keys enforce valid references. Unique constraints prevent duplicate supplier emails, category names, tag names, and warehouse locations. Domain checks protect non-negative prices and stock. Indexes target the join and filtering paths used by the updated queries.

## Query trade-off

The normalized model requires joins for category, supplier, tag, and inventory lookups. That adds query text and work compared with reading one wide row, but it removes duplicated values and makes writes consistent. The design chooses correctness and maintainability first; the indexes recover the common read paths without reintroducing denormalized data. If reporting later needs a stable cross-table snapshot, a materialized view can be added as a read model rather than copying values into the source tables.
