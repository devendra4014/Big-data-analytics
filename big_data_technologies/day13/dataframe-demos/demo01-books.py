
from pyspark.sql import SparkSession

spark = SparkSession.builder\
			.appName('demo01')\
			.config('spark.sql.shuffle.partitions', '4')\
			.getOrCreate()

file_path = 'file:///home/nilesh/sep22/dbda/bigdata/data/books_hdr.csv'
books = spark.read\
		.option('delimiter', ',')\
		.option('header', 'true')\
		.option('inferSchema', 'true')\
		.csv(file_path)

result = books\
		.select('subject', 'price')\
		.groupBy('subject').sum('price')\
		.orderBy('subject')

result.show()

input('press enter to exit...')

spark.stop()
