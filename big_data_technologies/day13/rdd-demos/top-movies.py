#!/usr/bin/python3

from pyspark import SparkConf, SparkContext, StorageLevel

conf = SparkConf()\
		.setAppName('top-movies')

sc = SparkContext(conf=conf)
sc.setCheckpointDir('file:///tmp/movie_ratings')


def parse_movie(line):
    try:
        parts = line.split('^')
        movie_id = int(parts[0])
        movie_title = parts[1]
        return (movie_id, movie_title)
    except:
        return ()


def parse_rating(line):
    try:
        parts = line.split(',')
        movie_id = int(parts[1])
        count = 1
        return (movie_id, count)
    except:
        return ()


movieFilePath = 'file:///tmp/movies/movies_caret.csv'
movies = sc.textFile(movieFilePath)\
            .map(lambda line: parse_movie(line))\
            .filter(lambda tup: len(tup) > 1)\

# movies.foreach(lambda record: print(record))

ratingFilePath = 'file:///tmp/movies/ratings.csv'
ratings = sc.textFile(ratingFilePath)\
            .map(lambda line: parse_rating(line))\
            .filter(lambda tup: len(tup) > 1)\
            .reduceByKey(lambda a,b: a + b)

# ratings.foreach(lambda record: print(record))

movie_ratings = movies.join(ratings)\
                    .sortBy(lambda tup: tup[1][1], ascending=False)\
                    .map(lambda tup: (tup[1][0], tup[1][1]))\

print('Number of partitions in movies: ', movies.getNumPartitions())
print('Number of partitions in ratings: ', ratings.getNumPartitions())
print('Number of partitions in movie_ratings: ', movie_ratings.getNumPartitions())

# movie_ratings.cache()
# movie_ratings.persist(StorageLevel.MEMORY_ONLY)
movie_ratings.checkpoint()

movie_ratings.foreach(lambda record: print(record))

# top_movie_ratingcount = movie_ratings.first()
# print('Top-most movie: ', top_movie_ratingcount)

# print('Top 10 movies:')
# top10_movie_ratingcounts = movie_ratings.take(10)
# for record in top10_movie_ratingcounts:
#     print(record)

print('Done!')

input('Press enter to exit ...')
sc.stop()