from airflow import DAG,utils
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import Connection
from airflow import settings
from datetime import timedelta, date
from os import path
import jdatetime
from datetime import  date
import pandas as pd


EXCEL_FILE_NAME="daily_trades"
EXCEL_FILE_EXT_XLSX = "xlsx"
EXCEL_FILE_EXT_CSV = "csv"
EXCEL_FILE_PATH = "/tmp"


#------------------------------------- Python  Functions -----------------------------------

def preprocess_convert_to_csv() :
    xlsx_file_path = path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, date.today().strftime("%Y_%m_%d"),EXCEL_FILE_EXT_XLSX))
    csv_file_path = path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, date.today().strftime("%Y_%m_%d"),EXCEL_FILE_EXT_CSV))
    df = pd.read_excel (xlsx_file_path, header=0, skiprows=2 , engine='openpyxl')
    today = jdatetime.date.today()
    df = df.assign(fa_date=today.strftime("%Y-%m-%d"))
    df = df.assign(en_date = date.today().isoformat())
    df = df.assign(fa_year = today.year)
    df.to_csv (csv_file_path, index = None, header=True,encoding="utf-8")
    print("%"*20)
    print(f"{csv_file_path} created sucessfully!")
    print("%"*20)
    


#--------------------------------------------------------------------------------

default_args = {
    "owner": "nikamooz",
    "depends_on_past": False,
    # "start_date": datetime(2020, 9, 30),
    'start_date': utils.dates.days_ago(1), 
    "email": ["smbanaei@ut.ac.ir"],
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG("Stock-Exchange-V2", default_args=default_args, schedule_interval="0 13 * * 6,0-3" , catchup=False );

task_read_stock_exchange_xlsx_file = BashOperator(
    task_id='Download-Stock-Exchange-Xlsx-File',
    bash_command='curl --retry 10 --output {0} -L -H "User-Agent:Chrome/61.0" --compressed "http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=0"'.format( path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, date.today().strftime("%Y_%m_%d"),EXCEL_FILE_EXT_XLSX))),
    dag=dag,
)

task_waiting_file_xlsx = FileSensor(task_id="Waiting-Excel-File",
                                    fs_conn_id="fs_temp",
                                    filepath = path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, date.today().strftime("%Y_%m_%d"),EXCEL_FILE_EXT_XLSX)),
                                    poke_interval = 10, # every 10 seconds,
                                    dag = dag
                                    )


task_dummy = DummyOperator(task_id="Dummy-Operator", dag=dag)


task_preprocess_convert_to_csv = PythonOperator(
    task_id='Preprocess-Convert_To_CSV',
    python_callable=preprocess_convert_to_csv,
    dag=dag,
)

#  ----------------------- DAG Structure -------------------------------

task_read_stock_exchange_xlsx_file >> task_waiting_file_xlsx >> task_preprocess_convert_to_csv >>task_dummy

#--------------------------------------------------------------------------

