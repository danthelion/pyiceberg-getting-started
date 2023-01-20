import os

from pyiceberg.catalog import load_catalog
from pyiceberg.expressions import GreaterThanOrEqual
from pyiceberg.partitioning import PartitionSpec, PartitionField
from pyiceberg.schema import Schema
from pyiceberg.table.sorting import SortOrder, SortField
from pyiceberg.transforms import DayTransform
from pyiceberg.transforms import IdentityTransform
from pyiceberg.types import (
    TimestampType,
    DoubleType,
    StringType,
    NestedField,
    IntegerType,
)


def query_table(namespace, table_name):
    table = CATALOG.load_table((namespace, table_name))

    print(f"Querying {table.name()}")

    con = table.scan().to_duckdb(table_name="distant_taxi_trips")

    print(con.execute("SELECT * FROM distant_taxi_trips LIMIT 4").fetchall())


def create_namespace_if_not_exists(namespace):
    if (namespace,) not in CATALOG.list_namespaces():
        print(CATALOG.list_namespaces())
        CATALOG.create_namespace(namespace)


def create_table_if_not_exists(namespace, table_name):
    if (namespace, table_name) not in CATALOG.list_tables(namespace):
        schema = Schema(
            NestedField(
                field_id=1, name="VendorId", field_type=IntegerType(), required=False
            ),
            NestedField(
                field_id=2,
                name="tpepPickupDateTime",
                field_type=TimestampType(),
                required=False,
            ),
            NestedField(
                field_id=3,
                name="tpepDropoffDateTime",
                field_type=TimestampType(),
                required=False,
            ),
            NestedField(
                field_id=4,
                name="passengerCount",
                field_type=IntegerType(),
                required=False,
            ),
            NestedField(
                field_id=5, name="tripDistance", field_type=DoubleType(), required=False
            ),
            NestedField(
                field_id=6,
                name="puLocationId",
                field_type=IntegerType(),
                required=False,
            ),
            NestedField(
                field_id=7,
                name="doLocationId",
                field_type=IntegerType(),
                required=False,
            ),
            NestedField(
                field_id=8, name="rateCodeId", field_type=IntegerType(), required=False
            ),
            NestedField(
                field_id=9,
                name="storeAndFwdFlag",
                field_type=StringType(),
                required=False,
            ),
            NestedField(
                field_id=10,
                name="paymentType",
                field_type=IntegerType(),
                required=False,
            ),
            NestedField(
                field_id=11, name="fareAmount", field_type=DoubleType(), required=False
            ),
            NestedField(
                field_id=12, name="extra", field_type=DoubleType(), required=False
            ),
            NestedField(
                field_id=13, name="mtaTax", field_type=DoubleType(), required=False
            ),
            NestedField(
                field_id=14,
                name="improvementSurcharge",
                field_type=DoubleType(),
                required=False,
            ),
            NestedField(
                field_id=15, name="tipAmount", field_type=DoubleType(), required=False
            ),
            NestedField(
                field_id=16, name="tollsAmount", field_type=DoubleType(), required=False
            ),
            NestedField(
                field_id=17, name="totalAmount", field_type=DoubleType(), required=False
            ),
            NestedField(
                field_id=18, name="puYear", field_type=IntegerType(), required=False
            ),
            NestedField(
                field_id=19, name="puMonth", field_type=IntegerType(), required=False
            ),
        )

        partition_spec = PartitionSpec(
            PartitionField(
                source_id=1,
                field_id=1000,
                transform=DayTransform(),
                name="datetime_day",
            )
        )

        sort_order = SortOrder(SortField(source_id=4, transform=IdentityTransform()))

        if ("test", "trips") in CATALOG.list_tables("test"):
            CATALOG.drop_table("test.trips")
            print(CATALOG.list_tables("test"))

        CATALOG.create_table(
            identifier="test-namespace.trips",
            location="s3a://nyc-taxi-trips",
            schema=schema,
            partition_spec=partition_spec,
            sort_order=sort_order,
        )


if __name__ == "__main__":
    # Set AWS minio creds
    os.environ["AWS_ACCESS_KEY_ID"] = "minio"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"
    CATALOG = load_catalog("default")
    # create_namespace_if_not_exists(namespace="test-namespace")
    # create_table_if_not_exists(namespace="test-namespace", table_name="trips")
    query_table(namespace="test", table_name="trips")
