from extract_data import extract_data
from transform_data import transform_data
from load_data import load_data
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def etl_process():
    crm_data, sales_data, customer_service_data = extract_data()
    transformed_data = transform_data(crm_data, sales_data, customer_service_data)
    load_data(transformed_data)

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2030, 10, 26),
    'depends_on_past': False
}

# Create the DAG
with DAG(
    dag_id='etl_dag',
    default_args=default_args,
    description='An ETL DAG for processing customer data',
    schedule_interval='@yearly',  # Runs every year
    catchup=False,
) as dag:

    etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=etl_process
    )

etl_task