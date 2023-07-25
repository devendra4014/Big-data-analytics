
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

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

# result = emps.select('ename', 'sal', 'comm')\
# 			.withColumn('income', expr('sal + IFNULL(comm, 0.0)'))

# result = emps.selectExpr('ename', 'sal', 'comm', 'sal + IFNULL(comm, 0.0) AS income')

# result = emps.selectExpr('*', 'sal + IFNULL(comm, 0.0) AS income')

# result = emps.selectExpr('job', 'sal + IFNULL(comm, 0.0) AS income')\
# 			.groupby('job').avg('income')\
# 			.withColumnRenamed('avg(income)', 'income_avg')

# SELECT deptno, job, COUNT(1) FROM emp GROUP BY deptno, job;
# result = emps.select('deptno', 'job')\
# 			.groupby('deptno', 'job').count()

# SELECT job, SUM(sal), AVG(sal), MAX(sal), MIN(sal) FROM emp GROUP BY job;
result = emps.select('job', 'sal')\
			.groupby('job')\
			.agg(sum('sal').alias('salsum'), avg('sal').alias('salavg'), max('sal').alias('salmax'), min('sal').alias('salmin'))

# result.show(truncate=False)

# result.write\
# 	.mode('OVERWRITE')\
# 	.csv('file:///tmp/output')

# result.write\
# 	.mode('OVERWRITE')\
# 	.json('file:///tmp/output')

# result.write\
# 	.mode('OVERWRITE')\
# 	.orc('file:///tmp/output')

# result.write\
# 	.mode('OVERWRITE')\
# 	.parquet('file:///tmp/output')

result.write\
	.mode('OVERWRITE')\
	.option('user', 'nilesh')\
	.option('password', 'nilesh')\
	.jdbc(url='jdbc:mysql://localhost:3306/test', table='emp_summary')
print('Done!!')

spark.stop()