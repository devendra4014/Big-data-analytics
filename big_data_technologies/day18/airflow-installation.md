# Airflow Installation

* step 1: Install pre-requisites
```sh
terminal> sudo apt-get update
```

```sh
terminal> sudo apt-get install build-essential
```

```sh
terminal> sudo apt-get install -y --no-install-recommends \
freetds-bin \
ldap-utils \
libffi7 \
libsasl2-2 \
libsasl2-modules \
libssl1.1 \
locales \
lsb-release \
sasl2-bin \
sqlite3 \
unixodbc \
mysql-server

terminal> sudo apt-get install libmysqlclient-dev
```

* step 2: Install airflow
	* In ~/.bashrc append,
		```sh
		alias python='python3'
		```
	* Run following commands in new terminal.
		```sh
		terminal> AIRFLOW_VERSION=2.5.1
		
		terminal> PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

		terminal> CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

		terminal> echo $CONSTRAINT_URL
		```
	* Verify if $CONSTRAINT_URL is present (hit link in browser).
	* Launchpadlib 1.10.6 requires testresources, so use below command
		```sh
		terminal> sudo apt install python3-testresources
		```
	* Continue following commands in the same terminal.
		```sh
		terminal> mkdir ~/airflow

		terminal> python -m pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

		terminal> python -m pip install "apache-airflow[mysql,jdbc,sendgrid,sqlite]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
		```
	* Initialize default airflow metastore.
		```sh
		terminal> airflow db init
		```
* step 3: Configure airflow metastore into mysql.
	* Login as root into MySQL.
		```sh
		terminal> sudo mysql -u root
		```
	* Create metastore database and user with appropriate permissions. Give following commands with root user login.
		```SQL
		CREATE DATABASE airflow;

		CREATE USER airflow@'%'  IDENTIFIED BY 'airflow';

		GRANT ALL ON airflow.* TO airflow@'%';

		FLUSH PRIVILEGES;

		EXIT;
		```

* step 4: Configure Airflow.
	* In ~/airflow/airflow.cfg
		* Comment: # sql_alchemy_conn = sqlite:////home/sunbeam/airflow/airflow.db
		* And add: sql_alchemy_conn = mysql://airflow:airflow@localhost:3306/airflow
			* sql_alchemy_conn = mysql://mysql_user:mysql_password@localhost:3306/mysql_metastore_db
		* Comment # executor = SequentialExecutor
		* And add `executor = LocalExecutor`
		* Change: `load_examples = False`

* step 5: Start airflow and verify
	```sh
	terminal> airflow db init
	# to reset already created db --> airflow db reset
	
	terminal> airflow users create --username admin --firstname FirstName --lastname LastName --role Admin --email youremail@gmail.com
	
	#Enter new password for airflow
	password: 
	
	terminal_1> airflow webserver
	# In browser: http://localhost:8080/
	
	username: admin
	password: airflow password
	
	
	terminal_2> airflow scheduler

	terminal_3> ps aux | grep "airflow"
	```
