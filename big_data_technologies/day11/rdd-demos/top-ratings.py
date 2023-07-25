from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()\
        .setAppName('demo02')\
        .setMaster('spark://localhost:7077')
sc = SparkContext(conf=conf)

def parse_rating(line):
    try:
        parts = line.split(',')
        movie_rating = (int(parts[1]),float(parts[2]))
        return movie_rating
    except:
        movie_rating = ()
        return movie_rating


filePath = 'file:///tmp/movies/ratings.csv'
result = sc.textFile(filePath)\
            .map(lambda line:parse_rating(line))\
            .filter(lambda mr:len(mr) == 2)\
            .map(lambda mr: (mr[0],1))\
            .reduceByKey(lambda a,x: a + x)\
            .sortBy(lambda mc: mc[1], ascending=False)\
            .take(10)

for item in result:
    print(item)

sc.stop()
