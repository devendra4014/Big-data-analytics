from pyspark.sql import SparkSession

spark = SparkSession.builder\
			.appName('demo01')\
			.getOrCreate()

# source of the data
tweets_schema = 'id STRING, time STRING, text STRING'
tweets = spark.readStream\
			.format('json')\
			.schema(tweets_schema)\
			.option('path', 'file:///home/nilesh/sep22/dbda/new_tweets')\
			.load()

# processing
result = tweets\
			.selectExpr("EXPLODE(SPLIT(LOWER(text), '[^#a-z]')) AS word")\
			.where("word LIKE '#%' AND word != '#'")\
			.groupby("word").count()\
			.orderBy("count", ascending=False)\
			.limit(10)

# sink data
query = result.writeStream\
			.trigger(processingTime='10 seconds')\
			.format('console')\
			.option('truncate', 'false')\
			.outputMode('complete')\
			.start()

query.awaitTermination()

spark.stop()