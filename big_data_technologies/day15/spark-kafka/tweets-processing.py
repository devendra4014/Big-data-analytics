from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder\
			.appName('demo01')\
			.getOrCreate()

tweets = spark.readStream\
	.format('kafka') \
	.option('kafka.bootstrap.servers', '172.18.4.112:9092') \
	.option('subscribe', 'tweets') \
	.option('failOnDataLoss', 'false') \
	.option("startingOffsets", "earliest")\
	.load()
tweets.printSchema()

result = tweets\
	.selectExpr("CAST(value AS STRING) val")\
	.selectExpr("FROM_JSON(val, 'id BIGINT, time STRING, text STRING, author STRING') AS v")\
	.selectExpr("EXPLODE(SPLIT(LOWER(v.text), '[^#a-z]')) word")\
	.where("word LIKE '#%' AND word != '#'")\
	.groupby("word").count()\
	.orderBy("count", ascending=False)\
	.limit(10)

result.printSchema();

query = result.writeStream\
	.format('console')\
	.trigger(processingTime='5 seconds')\
	.option('truncate', 'false')\
	.outputMode('complete')\
	.start()

query.awaitTermination()

spark.stop()
