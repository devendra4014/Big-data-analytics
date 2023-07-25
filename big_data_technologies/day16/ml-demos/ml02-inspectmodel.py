from pyspark.sql import SparkSession

spark = SparkSession.builder\
			.appName('demo02')\
			.getOrCreate()

model_path = 'model1/data/part-00000-ecdd5771-a675-4e27-b751-59869805f128-c000.snappy.parquet'
model_df = spark.read\
	.parquet(model_path)

model_df.show(truncate=False)

spark.stop()
