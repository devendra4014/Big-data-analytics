from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import BinaryClassificationEvaluator

spark = SparkSession.builder\
			.appName('demo04')\
			.getOrCreate()

file_path = 'customers.csv'
data = spark.read\
		.option('delimiter', ',')\
		.option('header', 'true')\
		.option('inferSchema', 'true')\
		.csv(file_path)

df1 = data.withColumnRenamed('Purchased', 'label')\
		.drop('CustID')

genderIndexer = StringIndexer()\
	.setInputCol('Gender')\
	.setOutputCol('GenderIndexed')

vectAssembler = VectorAssembler()\
	.setInputCols(['Age', 'Salary', 'GenderIndexed'])\
	.setOutputCol('features')

model = LogisticRegression()

mlPipeline = Pipeline()\
	.setStages([genderIndexer, vectAssembler, model])

(train, test) = df1.randomSplit([0.7, 0.3])
trainedModel = mlPipeline.fit(train)
predictions = trainedModel.transform(test)

predictions.printSchema()
predictions.show(truncate=False, n=5)

accuracy = BinaryClassificationEvaluator()\
	.evaluate(predictions)
print('Model Accuracy: ', accuracy)

trainedModel.save('model2')
print('ML Pipeline Saved.')

spark.stop()
