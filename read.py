from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("ReadFromHDFS").getOrCreate()

# Read the CSV file from HDFS into a DataFrame
df = spark.read.csv("hdfs://localhost:9000/test/write.csv", header=False, inferSchema=True)

# Show the DataFrame content
df.show()

# Stop the Spark session
spark.stop()