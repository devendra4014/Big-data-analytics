from pyspark.sql import SparkSession

spark = SparkSession.builder\
			.appName('demo01')\
			.config('spark.sql.shuffle.partitions', '4')\
			.config('javax.jdo.option.ConnectionURL', 'jdbc:derby:;databaseName=/home/nilesh/setup/bigdata/apache-hive-3.1.2-bin/metastore_db')\
			.config('javax.jdo.option.ConnectionDriverName', 'org.apache.derby.jdbc.EmbeddedDriver')\
			.config('javax.jdo.PersistenceManagerFactoryClass', 'org.datanucleus.api.jdo.JDOPersistenceManagerFactory')\
			.config('spark.sql.warehouse.dir', 'hdfs://localhost:9000/user/hive/warehouse')\
			.enableHiveSupport()\
			.getOrCreate()

db = spark.catalog.currentDatabase()
print('Current Database: ', db)

tables = spark.catalog.listTables('dbda')
for tbl in tables:
	print(tbl)
	
contacts = spark.read.table('dbda.contacts')

result = contacts

result.show(truncate=False)

print('Done!!')
spark.stop()
