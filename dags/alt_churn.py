# скопируйте код ниже #
# dags/alt_churn.py

from airflow import DAG
from airflow.operators.python import PythonOperator
# продолжите код и запустите его в виртуальной машине #
# после отработки кода нажмите кнопку Проверить, добавлять свое решение необязательно #

with DAG(
    dag_id='churn_alt',
    schedule='@once',
    on_success_callback=send_telegram_success_message,
    on_failure_callback=send_telegram_failure_message) as dag:
    
    # код DAG #
    extract_step = PythonOperator(task_id='extract', python_callable=extract)
    transform_step = PythonOperator(task_id='transform', python_callable=transform)
    load_step = PythonOperator(task_id='load', python_callable=load)
    
    extract_step >> transform_step >> load_step