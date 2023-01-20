- What's a table format anyway
- When to use iceberg
- How? this post
  - docker upppoo
  - docker exec load data
    - this creates the icebergerino table
  - explore minio
  - explore metadata
  - python query
  - duckdb lmao!!

# Getting started with Iceberg using Python

## Introduction

Apache Iceberg is an open table format for huge analytic datasets. It is designed to replace the table formats of the
past, like Parquet and Avro, with a new format that adds features to support data lakes. Iceberg adds to the table
format a specification for a metastore to manage tables called the Iceberg table spec. This allows Iceberg to support
many different table layouts and file formats, including columnar formats like Parquet and ORC.

Iceberg is designed to improve on the shortcomings of existing table formats by adding support for missing features