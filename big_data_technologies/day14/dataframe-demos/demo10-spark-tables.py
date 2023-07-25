from pyspark.sql import SparkSession

spark = SparkSession.builder\
			.appName('demo01')\
			.config('spark.sql.shuffle.partitions', '4')\
			.getOrCreate()

file_path = 'file:///home/nilesh/sep22/dbda/bigdata/data/emp.csv'
emps_schema = 'empno INT, ename STRING, job STRING, mgr INT, hire DATE, sal DOUBLE, comm DOUBLE, deptno INT'
emps = spark.read\
		.schema(emps_schema)\
		.option('header', 'false')\
		.option('inferSchema', 'false')\
		.option('mode', 'DROPMALFORMED')\
		.option('nullValue', 'NULL')\
		.csv(file_path)
emps.printSchema()

# emps.write\
# 	.saveAsTable('emp')

# emps.write\
# 	.partitionBy('deptno')\
# 	.saveAsTable('emp_dept_part')

# emps.write\
# 	.partitionBy('deptno', 'job')\
# 	.saveAsTable('emp_dept_job_part')

# emps.write\
# 	.bucketBy(numBuckets=2, col='empno')\
# 	.saveAsTable('emp_bucketed')

# emps.write\
# 	.partitionBy('deptno')\
# 	.bucketBy(2, 'empno')\
# 	.saveAsTable('emp_dept_part_bucketed')

## In this application, data is stored in spark-warehouse, but
## metastore is not stored anywhere (was in memory only).
## So, though data of tables is available in warehouse, it cannot be
## read by due to unavailbility of the metadata.
emp_df = spark.read.table('emp')
emp_df.show(truncate=False)

print('Done!!')

spark.stop()
