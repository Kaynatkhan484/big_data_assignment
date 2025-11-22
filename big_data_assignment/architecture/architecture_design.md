# Big Data Architecture — Proposed Design

1. Data Sources: Large CSV/JSON datasets.
2. Ingestion: PySpark ingestion, schema inference, CSV → Parquet.
3. Storage: Raw CSV, Curated Parquet.
4. API: FastAPI with credit-control.
5. Scaling: Spark cluster, ClickHouse/BigQuery, Redis cache.
