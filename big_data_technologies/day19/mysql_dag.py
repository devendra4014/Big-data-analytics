
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator

dag_arg = {
    'owner': 'nilesh',
    'retries': '5',
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id = 'mysql_demo',
    default_args = dag_arg,
    schedule_interval = timedelta(hours=4),
    start_date = datetime(2023, 1, 31),
    end_date = datetime(2023, 2, 28),
    catchup=True
) as dag:
    task1 = MySqlOperator(
        task_id = 'create_mysql_table',
        mysql_conn_id = 'mysql_db',
        sql = r"""
            CREATE TABLE IF NOT EXISTS my_table(
                dt DATE,
                dag_id VARCHAR(50)
            );
        """
    )
    task2 = MySqlOperator(
        task_id = 'insert_mysql_table',
        mysql_conn_id = 'mysql_db',
        sql = r"""
            INSERT INTO my_table VALUES('{{ ds }}', 'Running: {{ dag.dag_id }}');
        """
    )

task1 >> task2
