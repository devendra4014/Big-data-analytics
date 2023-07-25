from pyspark.sql import SparkSession, Row
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.feature import StringIndexer, VectorAssembler

spark = SparkSession.builder\
			.appName('demo03')\
			.getOrCreate()


def prepare_data(gender, sal, age):
	customer_schema = 'CustID INT, Age INT, Salary DOUBLE, Gender STRING, Purchased INT'
	row = Row(0, age, sal, gender, 0)
	data = spark.createDataFrame([row], customer_schema)
	
	df1 = data \
		.withColumnRenamed('Purchased', 'label') \
		.drop('CustID')
	
	genderDF = spark.createDataFrame([[('Female')], [('Male')]], ['Gender'])
	genderIndexer = StringIndexer() \
		.setInputCol('Gender') \
		.setOutputCol('GenderIndexed')
	df2 = genderIndexer.fit(genderDF) \
		.transform(df1)
	
	vectAssembler = VectorAssembler() \
		.setInputCols(['Age', 'Salary', 'GenderIndexed']) \
		.setOutputCol('features')
	df3 = vectAssembler.transform(df2)
	
	df4 = df3.select('features', 'label')
	return df4

model_path = 'model1'
model = LogisticRegressionModel.load(model_path)

while True:
	age = int(input('Age (0 for Exit): '))
	if age == 0:
		break
	gender = input('Enter Gender (Male/Female): ')
	sal = float(input('Salary: '))
	data = prepare_data(gender, sal, age)
	
	predictions = model.transform(data)
	# predictions.show(truncate=False)
	row = predictions.select('prediction')\
			.first()
	pred = float(row[0])
	if pred == 0.0:
		print('Will Not Purchase')
	else:
		print('Will Purchase')

spark.stop()