import os

# 🔥 FIX: Stop Spark from searching for Hadoop on Windows
os.environ["HADOOP_HOME"] = "C:\\tmp"
os.environ["hadoop.home.dir"] = "C:\\tmp"

from pyspark.sql import SparkSession

# Start Spark
spark = SparkSession.builder \
    .appName("BigDataIngestionDemo") \
    .master("local[*]") \
    .getOrCreate()

print("[LOG] Spark session started")

# Load CSV file
df = spark.read.csv("sample_data.csv", header=True, inferSchema=True)
print("[LOG] Data loaded")

df.show(10)
df.printSchema()

# Save as Parquet
df.write.mode("overwrite").parquet("../output/parquet")
print("[LOG] Parquet conversion completed")
