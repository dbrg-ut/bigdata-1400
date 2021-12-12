from airflow import DAG,utils
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
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
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG("Stock-Exchange-V0", default_args=default_args, schedule_interval="0 14 * * 6,0-3" , catchup=False );
# dag = DAG("Stock-Exchange-V0", default_args=default_args, schedule_interval=timedelta(minutes=5) , catchup=False );

read_stock_exchange_xlsx_file = BashOperator(
    task_id='Download-Stock-Exchange-Xlsx-File',
    bash_command='curl --retry 10 --output {0} -L -H "User-Agent:Chrome/61.0" --compressed "http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=0"'.format( path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, date.today().strftime("%Y_%m_%d"),EXCEL_FILE_EXT))),
    dag=dag,
)

read_stock_exchange_xlsx_file