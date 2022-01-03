import os
import json
import requests
import pytz

from datetime import date, datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.decorators import dag, task
from airflow.models import Variable

DAG_NAME = os.path.basename(__file__).replace(".py", "")

default_args = {
    'owner': 'maxime.jumelle',
    'depends_on_past': False,
    'start_date': days_ago(0, hour=1),
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

@dag(DAG_NAME, default_args=default_args, schedule_interval="0 * * * *", tags=["sysops"])
def dag_test():
    """
    Say Hello !
    """
    @task()
    def hello():
      print("Hello !")
    
    hello()

test = dag_test()