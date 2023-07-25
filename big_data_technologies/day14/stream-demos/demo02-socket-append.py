#!/usr/bin/pyspark3

from pyspark.sql import SparkSession

spark = SparkSession.builder\
			.appName('demo01')\
			.getOrCreate()

# source of the data
data = spark.readStream\
			.format('socket')\
			.option('host', '127.0.0.1')\
			.option('port', '4444')\
			.load()

data.printSchema()

# processing on the data
result = data\
			.selectExpr("EXPLODE(SPLIT(LOWER(value), '[^a-z]')) AS word")\
			.where("word NOT IN ('', 'you', 'is', 'are', 'a', 'the', 'shall', 'for', 'of')")

# sink data
query = result.writeStream\
			.trigger(processingTime='10 seconds')\
			.format('console')\
			.outputMode('append')\
			.start()

query.awaitTermination()

spark.stop()
