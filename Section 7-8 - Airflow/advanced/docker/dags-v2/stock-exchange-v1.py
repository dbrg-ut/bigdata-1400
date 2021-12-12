from airflow import DAG,utils
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.models import Connection
from airflow import settings
from os import path
from datetime import  date

EXCEL_FILE_NAME="daily_trades"
EXCEL_FILE_EXT = "xlsx"
EXCEL_FILE_PATH = "/tmp"

default_args = {
    "owner": "nikamooz",
    "depends_on_past": False,
    # "start_date": datetime(2020, 9, 30),
    'start_date': utils.dates.days_ago(3), 
    "email": ["smbanaei@ut.ac.ir"],
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG("Stock-Exchange-V1", default_args=default_args, schedule_interval="0 13 * * 6,0-3" , catchup=False );

task_read_stock_exchange_xlsx_file = BashOperator(
    task_id='Download-Stock-Exchange-Xlsx-File',
    bash_command='curl --retry 10 --output {0} -L -H "User-Agent:Chrome/61.0" --compressed "http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=0"'.format( path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, date.today().strftime("%Y_%m_%d"),EXCEL_FILE_EXT))),
    dag=dag,
)

task_waiting_file_xlsx = FileSensor(task_id="Waiting-Excel-File",
                                    fs_conn_id="fs_temp",
                                    filepath = path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, date.today().strftime("%Y_%m_%d"),EXCEL_FILE_EXT)),
                                    poke_interval = 10, # every 10 seconds,
                                    dag = dag
                                    )


task_dummy = DummyOperator(task_id="Dummy-Operator", dag=dag)
task_dummy2 = DummyOperator(task_id="Dummy-Operator-2", dag=dag)
task_dummy3 = DummyOperator(task_id="Dummy-Operator-3", dag=dag)

task_read_stock_exchange_xlsx_file >> task_waiting_file_xlsx >> [task_dummy , task_dummy2] >> task_dummy3
