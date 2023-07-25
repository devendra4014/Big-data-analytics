from datetime import datetime, timedelta
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python_operator import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator

def clean_store_data():
    import pandas as pd
    import re

    df = pd.read_csv("/tmp/input/stores.csv")

    def clean_store_location(st_loc):
        return re.sub(r'[^\w\s]', '', st_loc).strip()

    def clean_product_id(pd_id):
        matches = re.findall(r'\d+', pd_id)
        if matches:
            return matches[0]
        return pd_id

    def remove_dollar(amount):
        return float(amount.replace('$', ''))

    df['STORE_LOCATION'] = df['STORE_LOCATION'].map(lambda x: clean_store_location(x))
    df['PRODUCT_ID'] = df['PRODUCT_ID'].map(lambda x: clean_product_id(x))

    for to_clean in ['MRP', 'CP', 'DISCOUNT', 'SP']:
        df[to_clean] = df[to_clean].map(lambda x: remove_dollar(x))

    df.to_csv('/tmp/input/clean_stores.csv', index=False)


dag_args = {
    'owner': 'nilesh',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
    'start_date': datetime(2022, 8, 21),
    'end_date': datetime(2022, 8, 28)
}

with DAG(
        dag_id='report_process_v4', 
        default_args=dag_args, 
        schedule_interval=None,
        catchup=False
) as dag:
    task1 = FileSensor(
                task_id = 'check_input_file', 
                poke_interval = 30,
                filepath = '/tmp/input/stores.csv' 
            )
    task2 = PythonOperator(
                task_id = 'clean_input_csv', 
                python_callable = clean_store_data
            )
    task3 = BashOperator(
                task_id = 'delete_input_file', 
                bash_command = "rm /tmp/input/stores.csv"
            )
    task4 = MySqlOperator(
                task_id = 'create_mysql_table', 
                mysql_conn_id = "mysql_local", 
                sql = r"""
                    CREATE TABLE IF NOT EXISTS store_transactions(store_id VARCHAR(50), store_location VARCHAR(50), product_category VARCHAR(50), product_id INT, mrp FLOAT, cp FLOAT, discount FLOAT, sp FLOAT, sdate DATE);
                """
            )
    task5 = MySqlOperator(
                task_id = 'insert_into_table', 
                mysql_conn_id = "mysql_local", 
                sql = r"""
                    LOAD DATA LOCAL INFILE '/tmp/input/clean_stores.csv' INTO TABLE store_transactions FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
                """
            )
    task6 = BashOperator(
                task_id = 'delete_clean_file', 
                bash_command = "rm /tmp/input/clean_stores.csv"
            )
    task7 = EmailOperator(
        task_id = 'send_email',
        to = 'ghule.nilesh@gmail.com',
        subject = 'Data Ingestion',
        html_content = r""" 
        Daily Report,
            Store data is cleaned and ingested successfully on {{ds}}.
        """
    )

task1 >> task2 >> task3 >> task4 >> task5 >> task6 >> task7

