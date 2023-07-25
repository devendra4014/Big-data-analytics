
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

dag_arg = {
    'owner': 'nilesh',
    'retries': '5',
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id = 'second',
    default_args = dag_arg,
    schedule_interval = '@daily',
    start_date = datetime(2023, 1, 28),
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = 'sleep 2 && echo "This is First Task."'
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = 'sleep 5 && echo "This is Second Task."'
    )

    task3 = BashOperator(
        task_id = 'third_task',
        bash_command = 'sleep 3 && echo "This is Third Task."'
    )

    task4 = BashOperator(
        task_id = 'fourth_task',
        bash_command = 'sleep 1 && echo "This is Fourth Task."'
    )

    task5 = BashOperator(
        task_id = 'fifth_task',
        bash_command = 'sleep 2 && echo "This is Fifth Task."'
    )

task1 >> [task2, task3] >> task4 >> task5
