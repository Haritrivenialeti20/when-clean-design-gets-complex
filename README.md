# When Clean Design Gets Complex — Database Normalization Challenge

This submission redesigns the original e-commerce schema to Third Normal Form while preserving the product query use cases.

## Deliverables

- `schema/broken_schema.sql` — the supplied baseline, retained for comparison.
- `schema/normalized_schema.sql` — the corrected 3NF schema.
- `queries/product_queries.sql` — five working queries rewritten with explicit joins.
- `queries/product_queries.original.sql` — the supplied query baseline.
- `docs/normalization-review.md` — 1NF, 2NF, and 3NF findings plus the normalization/performance trade-off.
- `docs/normalized-er.png` and `docs/normalized-er.mmd` — normalized relationship diagram and source.
- `docs/query-results.png` — screenshot-style evidence of the verified query results.
- `scripts/verify_queries.py` — reproducible SQLite verification harness with sample data.

## What changed

The original `products` table stored comma-separated categories and tags, supplier attributes, and warehouse inventory in one row. The new design separates those concerns into `suppliers`, `categories`, `tags`, `warehouses`, and relationship/fact tables: `product_categories`, `product_tags`, and `inventory`. Primary keys, foreign keys, unique constraints, non-negative checks, and targeted indexes protect the normalized model.

The query file now uses joins for category filtering, supplier lookups, low-stock inventory, and tag search. This increases query complexity by making relationships explicit, but eliminates update anomalies and makes the design scalable and maintainable.

## Verification

Run the included harness:

```bash
python3 scripts/verify_queries.py
```

It loads the schema with foreign-key enforcement enabled, inserts representative sample data, and executes all five normalized queries. The expected result is five successful query checks.
