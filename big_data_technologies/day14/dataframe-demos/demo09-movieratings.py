from pyspark.sql import SparkSession

spark = SparkSession.builder\
			.appName('demo01')\
			.config('spark.sql.shuffle.partitions', '4')\
			.getOrCreate()

rating_file_path = 'file:///tmp/ratings/ratings.csv'
ratings = spark.read\
			.option('delimiter', ',')\
			.option('header', 'true')\
			.option('inferSchema', 'true')\
			.csv(rating_file_path)
ratings.printSchema()

result = ratings\
			.selectExpr('YEAR(FROM_UNIXTIME(`timestamp`)) AS yr')\
			.groupby('yr').count()

result.printSchema()
result.show(truncate=False)

spark.stop()