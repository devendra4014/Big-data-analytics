from pyspark.sql import SparkSession

## In this application, data is stored in metastore given by "spark.sql.warehouse.dir"
## The metastore is stored in derby given by "javax.jdo.option.ConnectionURL"

spark = SparkSession.builder\
			.appName('demo01')\
			.config('spark.sql.shuffle.partitions', '4')\
			.config('javax.jdo.option.ConnectionURL', 'jdbc:derby:;databaseName=/home/nilesh/spark/metastore_db;create=true')\
			.config('javax.jdo.option.ConnectionDriverName', 'org.apache.derby.jdbc.EmbeddedDriver')\
			.config('javax.jdo.PersistenceManagerFactoryClass', 'org.datanucleus.api.jdo.JDOPersistenceManagerFactory')\
			.config('spark.sql.warehouse.dir', 'file:///home/nilesh/spark/spark-warehouse')\
			.enableHiveSupport()\
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
# 	.saveAsTable('emp_all')

emp_df = spark.read.table('emp_all')

emp_df\
	.groupby('job').avg('sal')\
	.show(truncate=False)
emp_df.explain(True)

# db = spark.catalog.currentDatabase()
# print('Current Database: ', db)
#
# tables = spark.catalog.listTables()
# for tbl in tables:
# 	print(tbl)

print('Done!!')

spark.stop()
