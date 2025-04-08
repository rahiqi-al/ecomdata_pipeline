from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'ali & imad',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('ecomdata_pipeline',default_args=default_args, schedule_interval='@hourly', start_date=days_ago(1),catchup=False) as dag:

    generate_data = BashOperator(task_id='generate_data',bash_command='python /project/scripts/generate_data.py')

    generate_data

 