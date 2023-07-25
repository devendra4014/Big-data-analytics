
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()\
		.setAppName('wordcount')\
		.setMaster('local[2]')
sc = SparkContext(conf=conf)


article_counter = sc.accumulator(0)
stopwords_list = ['','a','an','the','is','are','shall','of','for','by', 'as']
stopwords = sc.broadcast(stopwords_list)


def count_articles(word):
	if word == 'a' or word == 'an' or word == 'the':
		article_counter.add(1)
	return word


filePath = 'file:///home/nilesh/setup/bigdata/spark-3.3.1-bin-hadoop3/LICENSE'
result = sc.textFile(filePath)\
			.map(lambda line: line.lower())\
			.flatMap(lambda line: line.split())\
			.map(lambda word: count_articles(word))\
			.filter(lambda word: word not in stopwords.value)\
			.map(lambda word: (word,1))\
			.reduceByKey(lambda a,x: a + x)\
			.map(lambda wc: (wc[0].upper(), wc[1]))\
			.sortBy(lambda wc: wc[1], ascending=False)\
			.take(20)

for item in result:
	print(item)

print('Article Count: ', article_counter.value)
sc.stop()
