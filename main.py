import os

from pyiceberg.catalog import load_catalog


def query_table(namespace, table_name):
    table = CATALOG.load_table((namespace, table_name))

    print(f"Querying {table.name()}")

    print(f"Describing: {table.schema()}")

    print(f"Partition spec: {table.spec()}")

    print(f"Files: {table.current_snapshot()}")


    con = table.scan().to_duckdb(table_name="distant_taxi_trips")

    print(con.execute("SELECT * FROM distant_taxi_trips LIMIT 4").fetchall())


if __name__ == "__main__":
    os.environ["AWS_ACCESS_KEY_ID"] = "minio"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"
    CATALOG = load_catalog("default")
    query_table(namespace="nyctaxi3", table_name="trips")
