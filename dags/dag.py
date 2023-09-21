from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from extract import extract_data
from transformation import transform_data
from load import load_data

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "data_pipeline_dag",
    default_args=default_args,
    description="A simple data pipeline example",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 9, 20),
    catchup=False,
) as dag:
    t1 = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )

    t2 = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
    )

    t3 = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

t1.set_downstream(t2)
t2.set_downstream(t3)
