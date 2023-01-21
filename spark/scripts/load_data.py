from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)

df = spark.read.parquet("/home/iceberg/data/yellow_tripdata_2022-01.parquet")
df.write.saveAsTable("nyctaxi2.trips", format="iceberg")
