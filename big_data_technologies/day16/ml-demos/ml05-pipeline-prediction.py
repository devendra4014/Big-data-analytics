from pyspark.sql import SparkSession, Row
from pyspark.ml import PipelineModel

spark = SparkSession.builder \
	.appName('demo05') \
	.getOrCreate()


def prepare_data(gender, sal, age):
	customer_schema = 'CustID INT, Age INT, Salary DOUBLE, Gender STRING, Purchased INT'
	row = Row(0, age, sal, gender, 0)
	data = spark.createDataFrame([row], customer_schema)
	
	df1 = data \
		.withColumnRenamed('Purchased', 'label') \
		.drop('CustID')
	return df1


model_path = 'model2'
model = PipelineModel.load(model_path)

while True:
	age = int(input('Age (0 for Exit): '))
	if age == 0:
		break
	gender = input('Enter Gender (Male/Female): ')
	sal = float(input('Salary: '))
	data = prepare_data(gender, sal, age)
	
	predictions = model.transform(data)
	# predictions.show(truncate=False)
	row = predictions.select('prediction') \
		.first()
	pred = float(row[0])
	if pred == 0.0:
		print('Will Not Purchase')
	else:
		print('Will Purchase')

spark.stop()
