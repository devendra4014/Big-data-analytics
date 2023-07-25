from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder\
			.appName('demo01')\
			.config('spark.sql.shuffle.partitions', '4')\
			.getOrCreate()

file_path = 'file:///home/nilesh/sep22/dbda/bigdata/data/ncdc'
ncdc = spark.read\
			.format('text')\
			.option('path', file_path)\
			.load()
# ncdc.printSchema()

regex = '^.{15}([0-9]{4}).{68}([-\\+][0-9]{4})([0-9]).*$'
readings = ncdc\
			.withColumn('yr', regexp_extract('value', regex, 1).cast('INT'))\
			.withColumn('temp', regexp_extract('value', regex, 2).cast('DOUBLE'))\
			.withColumn('quality', regexp_extract('value', regex, 3).cast('INT'))\
			.drop('value')\
			.repartition(4)
readings.printSchema()

# readings.show()
readings.write\
	.format('json')\
	.option('path', 'file:///tmp/output')\
	.mode('overwrite')\
	.save()

print('Done!!')

spark.stop()