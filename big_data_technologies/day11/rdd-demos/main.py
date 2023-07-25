
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()\
        .setAppName('demo01')\
        .setMaster('spark://localhost:7077')
sc = SparkContext(conf=conf)

filePath = 'file:///home/nilesh/setup/bigdata/spark-3.3.1-bin-hadoop3/LICENSE'
result = sc.textFile(filePath)\
            .map(lambda line: line.lower())\
            .flatMap(lambda line: line.split())\
            .map(lambda word: (word,1))\
            .reduceByKey(lambda a,x: a + x)\
            .map(lambda wc: (wc[0].upper(), wc[1]))\
            .sortBy(lambda wc: wc[1], ascending=False)\
            .take(20)

for item in result:
    print(item)

sc.stop()
