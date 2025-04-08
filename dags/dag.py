from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import os


default_args = {
    'owner': 'ali & imad',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)}

def check_staging_files():
    if os.listdir('/project/staging'):
        return 'send_files_message'
    return 'send_no_files_message'

with DAG('ecomdata_pipeline',default_args=default_args, schedule_interval='@hourly', start_date=days_ago(1),catchup=False) as dag:

    generate_data = BashOperator(task_id='generate_data',bash_command='python /project/scripts/generate_data.py')

    wait_for_nifi = BashOperator(task_id='wait_for_nifi',bash_command='sleep 30')

    branch_task = BranchPythonOperator(task_id='check_staging_files',python_callable=check_staging_files)

    send_no_files_message = BashOperator(task_id='send_no_files_message',bash_command='echo "$(date): No files in staging - pipeline worked" >> /project/logs/app.log')

    send_files_message = BashOperator(task_id='send_files_message',bash_command='echo "$(date): Files still in staging - pipeline failed" >> /project/logs/app.log')

    generate_data >> wait_for_nifi >> branch_task
    branch_task >> send_no_files_message
    branch_task >> send_files_message
 