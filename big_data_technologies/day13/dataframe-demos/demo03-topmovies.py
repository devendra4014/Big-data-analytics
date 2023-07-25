from pyspark.sql import SparkSession

spark = SparkSession.builder\
			.appName('demo01')\
			.config('spark.sql.shuffle.partitions', '4')\
			.getOrCreate()

movie_file_path = 'file:///tmp/movies/movies.csv'
movies = spark.read\
			.option('delimiter', ',')\
			.option('header', 'true')\
			.option('inferSchema', 'true')\
			.csv(movie_file_path)
movies.printSchema()

rating_file_path = 'file:///tmp/movies/ratings.csv'
ratings = spark.read\
			.option('delimiter', ',')\
			.option('header', 'true')\
			.option('inferSchema', 'true')\
			.csv(rating_file_path)
ratings.printSchema()

# result = ratings.join(movies, 'movieId')
result = ratings\
	.join(movies, [ratings.movieId == movies.movieId], 'inner')\
	.select('title', 'rating')\
	.groupby('title').count()\
	.orderBy('count', ascending=False)\
	.limit(10)

result.printSchema()

result.show(truncate=False)

result.explain(extended=True)

spark.stop()