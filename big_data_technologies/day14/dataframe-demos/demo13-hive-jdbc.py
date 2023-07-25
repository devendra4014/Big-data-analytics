from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder\
			.appName('demo01')\
			.config('spark.sql.shuffle.partitions', '4')\
			.getOrCreate()

wc = spark.read\
	.option('user', 'nilesh')\
	.option('password', '')\
	.jdbc(url='jdbc:hive2://localhost:10000/dbda', table='wordcount')

result = wc

result.show(truncate=False)

spark.stop()
