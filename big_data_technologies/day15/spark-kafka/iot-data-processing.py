from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder\
			.appName('demo01')\
			.getOrCreate()

readings = spark.readStream\
	.format('kafka') \
	.option('kafka.bootstrap.servers', 'localhost:9092') \
	.option('subscribe', 'iot') \
	.option('failOnDataLoss', 'false') \
	.load()
# readings.printSchema()

result = readings\
	.selectExpr("CAST(value AS STRING) val")\
	.selectExpr("FROM_JSON(val, 'sensor STRING, reading INT, time STRING') v")\
	.selectExpr("v.sensor", "v.reading", "CAST(v.time AS TIMESTAMP) AS time")\
	.withWatermark("time", "10 seconds")\
	.groupby("sensor", window('time', windowDuration='20 seconds', slideDuration='10 seconds')).avg("reading")\
	.withColumnRenamed("avg(reading)", "avgreading")\
	.selectExpr("(sensor,window.start,window.end,avgreading) AS result")\
	.selectExpr("TO_JSON(result) AS value")

result.printSchema()

query1 = result.writeStream\
	.format('console')\
	.trigger(processingTime='5 seconds')\
	.outputMode('append')\
	.option('truncate', 'false')\
	.start()

query2 = result.writeStream\
	.format('kafka')\
	.outputMode('append') \
	.option('topic', 'avgiot') \
	.option('kafka.bootstrap.servers', 'localhost:9092') \
	.option('checkpointLocation', '/tmp/iotckpt') \
	.start()

spark.streams.awaitAnyTermination()

spark.stop()
