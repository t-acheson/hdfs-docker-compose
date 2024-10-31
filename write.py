from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("WriteToHDFS").getOrCreate()

# Create a DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "Value"]
df = spark.createDataFrame(data, columns)

# Write the DataFrame to HDFS
df.write.csv("hdfs://localhost:9000/test/write.csv")

# Stop the Spark session
spark.stop()