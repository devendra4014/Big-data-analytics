from pyspark.sql import SparkSession

spark = SparkSession.builder\
			.appName('demo01')\
			.config('spark.sql.shuffle.partitions', '4')\
			.getOrCreate()

movie_file_path = 'file:///tmp/movies/movies_caret.csv'
movies = spark.read\
			.option('delimiter', '^')\
			.option('header', 'true')\
			.csv(movie_file_path)
movies.printSchema()

result = movies\
			.selectExpr("explode(split(genres, '[|]')) AS genre")\
			.groupby('genre').count()\
			.orderBy('count', ascending=False)

result.show(truncate=False)

spark.stop()