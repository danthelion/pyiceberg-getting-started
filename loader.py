import pyspark

# This script loads the data/yellow_tripadata_2022-01.parquet file into a Spark DataFrame and saves it to an Iceberg table
# in the "default" namespace. The table is created if it does not exist.


def main():
    spark = (
        pyspark.sql.SparkSession.builder.appName("test")
        .config("spark.sql.catalog.default", "org.apache.iceberg.spark.SparkCatalog")
        .config(
            "spark.sql.catalog.default.type",
            "hadoop",
        )
        .config(
            "spark.sql.catalog.default.warehouse",
            "s3a://nyc-taxi-trips",
        )
        .config(
            "spark.sql.catalog.default.io-impl",
            "org.apache.iceberg.aws.s3.S3FileIO",
        )
        .config(
            "spark.sql.catalog.default.hive.metastore.warehouse.dir",
            "s3a://nyc-taxi-trips",
        )
        .config(
            "spark.sql.catalog.default.hive.metastore.uris",
            "thrift://localhost:9083",
        )
        .config(
            "spark.sql.catalog.default.hive.metastore.version",
            "3.1.2",
        )
        .config(
            "spark.sql.catalog.default.hive.metastore.client.factory.class",
            "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory",
        )
        .config(
            "spark.sql.catalog.default.aws.access.key.id",
            "AKIAIOSFODNN7EXAMPLE",
        )
        .config(
            "spark.sql.catalog.default.aws.secret.access.key
        )
        .config(
            "spark.sql.catalog.default.aws.region",
            "us-east-1",
        )
        .config(
            "spark.sql.catalog.default.aws.assume.role",
