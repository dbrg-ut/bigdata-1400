# 5: Backfill & Catchup
# {{ds}}

from airflow import DAG,utils
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import Connection
from airflow import settings
from airflow.hooks.webhdfs_hook import  WebHDFSHook
from datetime import timedelta, date
from os import path
import jdatetime
from datetime import  date
import pandas as pd


EXCEL_FILE_NAME="daily_trades"
EXCEL_FILE_EXT_XLSX = "xlsx"
EXCEL_FILE_EXT_CSV = "csv"
EXCEL_FILE_PATH = "/tmp"
HDFS_CSV_FOLDER = "/data/data_lake/stock/fa_year="


#--------------------------------------------------------------------------------

default_args = {
    "owner": "nikamooz",
    "depends_on_past": False,
    # "start_date": datetime(2020, 9, 30),
    'start_date': utils.dates.days_ago(10), 
    "email": ["smbanaei@ut.ac.ir"],
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
     'provide_context' : True,
}

dag = DAG("Stock-Exchange-V5", default_args=default_args, schedule_interval="0 13 * * 6,0-3" , catchup=True );


#------------------------------------ Python Functions---------------------------------------

def put_csv_to_hdfs(**kwargs) : 
    ti = kwargs['ti']
    fa_year =  ti.xcom_pull(key='fa_year')
    filename = kwargs['input_file']
    target_path= kwargs['target_path']+'\"'+str(fa_year)+'\"'
    hdfs_hook = WebHDFSHook(webhdfs_conn_id="webhdfs_default")
    print("---"*30)
    print(f"Input File : {filename}")
    print(f"Target Path : {target_path}")
    print("---"*30)
    hdfs_hook.load_file(filename,target_path)
     


def is_symbol(row) :
    try :
        return  int(''.join(filter(str.isdigit, row["نماد"]))) < 20
    except : 
        return True
    

def preprocess_convert_to_csv(**kwargs) :
    ti = kwargs['ti']
    ds = kwargs['ds']
    xlsx_file_path = path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, ds, EXCEL_FILE_EXT_XLSX))
    csv_file_path = path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, ds, EXCEL_FILE_EXT_CSV))
    df = pd.read_excel (xlsx_file_path, header=0, skiprows=2 , engine='openpyxl')
    today = jdatetime.date.today()
    df = df.assign(fa_date=today.strftime("%Y-%m-%d"))
    df = df.assign(en_date = date.today().isoformat())
    df = df.assign(fa_year = today.year)
    df = df[df.apply(is_symbol, axis=1)]
    df.to_csv (csv_file_path, index = None, header=True,encoding="utf-8")
    ti.xcom_push(key='fa_year', value=today.year)


task_read_stock_exchange_xlsx_file = BashOperator(
    task_id='Download-Stock-Exchange-Xlsx-File',
    bash_command='curl --retry 10 --output {0} -L -H "User-Agent:Chrome/61.0" --compressed "http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d={{{{ds}}}}"'.format( path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, '{{ds}}',EXCEL_FILE_EXT_XLSX))),
    dag=dag,
)

task_waiting_file_xlsx = FileSensor(task_id="Waiting-Excel-File",
                                    fs_conn_id="fs_temp",
                                    filepath = path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, '{{ds}}',EXCEL_FILE_EXT_XLSX)),
                                    poke_interval = 10, # every 10 seconds,
                                    dag = dag
                                    )


task_dummy = DummyOperator(task_id="Dummy-Operator", dag=dag)


task_preprocess_convert_to_csv = PythonOperator(
    task_id='Preprocess-Convert-To-CSV',
    python_callable=preprocess_convert_to_csv,
    dag=dag,
)

task_put_csv_to_hdfs = PythonOperator(
    task_id='Put-CSV-To-HDFS',
    python_callable=put_csv_to_hdfs,
    op_kwargs={'target_path': HDFS_CSV_FOLDER ,        # input arguments
               'input_file': path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, '{{ds}}',EXCEL_FILE_EXT_CSV)) },
    dag=dag,
)

task_remove_original_files = BashOperator(
    task_id='Delete-Stock-Exchange-Xlsx-File',
    bash_command='rm {0} {1}'.format( path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, '{{ds}}',EXCEL_FILE_EXT_XLSX)),
                                     path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, '{{ds}}',EXCEL_FILE_EXT_CSV))),
    dag=dag
)

#  ----------------------- DAG Structure -------------------------------

task_read_stock_exchange_xlsx_file >> task_waiting_file_xlsx >> task_preprocess_convert_to_csv 
task_preprocess_convert_to_csv >>task_put_csv_to_hdfs >> task_remove_original_files >> task_dummy

#--------------------------------------------------------------------------



