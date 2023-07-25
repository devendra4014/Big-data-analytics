
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

spark = SparkSession.builder\
			.appName('demo01')\
			.getOrCreate()

file_path = 'customers.csv'
data = spark.read\
		.option('delimiter', ',')\
		.option('header', 'true')\
		.option('inferSchema', 'true')\
		.csv(file_path)
# data.printSchema()
# data.show(n=3, truncate=False)

df1 = data\
		.withColumnRenamed('Purchased', 'label')\
		.drop('CustID')
# df1.printSchema()
# df1.show(n=3, truncate=False)

genderIndexer = StringIndexer()\
	.setInputCol('Gender')\
	.setOutputCol('GenderIndexed')
df2 = genderIndexer.fit(df1)\
	.transform(df1)
# df2.printSchema()
# df2.show(n=3, truncate=False)

vectAssembler = VectorAssembler()\
	.setInputCols(['Age', 'Salary', 'GenderIndexed'])\
	.setOutputCol('features')
df3 = vectAssembler.transform(df2)
# df3.printSchema()
# df3.show(n=3, truncate=False)

df4 = df3.select('features', 'label')
# df4.printSchema()
# df4.show(n=3, truncate=False)

(train, test) = df4.randomSplit([0.7, 0.3])

model = LogisticRegression().fit(train)
predictions = model.transform(test)
predictions.printSchema()
predictions.show(n=30, truncate=False)

accuracy = BinaryClassificationEvaluator()\
	.evaluate(predictions)
print('Model Accuracy: ', accuracy)

model.save('model1')
print('Model is saved.')

spark.stop()

