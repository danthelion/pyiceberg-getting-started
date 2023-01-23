from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)

df = spark.read.parquet("/home/iceberg/warehouse/yellow_tripdata_2022-01.parquet")
df.write.saveAsTable("nyctaxi3.trips", format="iceberg")
