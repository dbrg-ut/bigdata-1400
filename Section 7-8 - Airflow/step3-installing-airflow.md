**Run these commands in Linux/WSL shell**

please visit this address for more explanation : [Installation — Airflow Documentation (apache.org)](https://airflow.apache.org/docs/apache-airflow/stable/installation.html)

#### Install Python

```bash
sudo apt install python3 python3-pip virtualenv
```



#### Install Prerequisite

```bash
$ sudo apt update
$ sudo apt-get install -y --no-install-recommends \
        freetds-bin \
        krb5-user \
        ldap-utils \
        libffi7 \
        libsasl2-2 \
        libsasl2-modules \
        libssl1.1 \
        locales  \
        lsb-release \
        sasl2-bin \
        sqlite3 \
        unixodbc
```

*in ubuntu 20 replace `libffi6` with `libffi7`*



#### (Optional) Virtualenv : 

```bash
$ cd 
$ mkdir airflow-venv
$ cd airflow-venv
$ python3 -m virtualenv .
$ source bin/activate
.
.
.
.
$ deactivate
```

#### Install Airflow

```bash
$ AIRFLOW_VERSION=2.2.2
$ PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.6
$ CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.6.txt
$ pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```


#### Setup database / first DAG

```bash
$ airflow db init
$ airflow db --help
usage: airflow db [-h] COMMAND ...

Database operations

positional arguments:
  COMMAND
    check           Check if the database can be reached
    check-migrations
                    Check if migration have finished
    init            Initialize the metadata database
    reset           Burn down and rebuild the metadata database
    shell           Runs a shell to access the database
    upgrade         Upgrade the metadata database to latest version

optional arguments:
  -h, --help        show this help message and exit

$ airflow version
2.0.1

$  airflow users create \
          --username admin \
          --firstname Mojtaba \
          --lastname Banaei \
          --role Admin \
          --password admin \
          --email admin@example.org
$ airflow users list	  
id | username | email             | first_name | last_name | roles
===+==========+===================+============+===========+======
1  | admin    | admin@example.org | Mojtaba    | Banaei    | Admin
$ cd 
$ ls
$ cd airflow
$ ls -lh
-rw-r--r-- 1 mojtaba mojtaba  39K Feb 13 12:00 airflow.cfg
-rw-r--r-- 1 mojtaba mojtaba 536K Feb 13 12:06 airflow.db
drwxr-xr-x 4 mojtaba mojtaba 4.0K Feb 13 12:05 logs
-rw-r--r-- 1 mojtaba mojtaba 2.6K Feb 13 12:00 unittests.cfg
-rw-r--r-- 1 mojtaba mojtaba 4.6K Feb 13 12:00 webserver_config.py

$ mkdir dags
$ cp /mnt/?/Section7/dags/*.py   dags

$ nano airflow.cfg
 set : load_examples = False
 
```

#### Start Scheduler / Web Server

```bash
$ airflow scheduler
tweets-v0.py  ____________       _____________
 ____    |__( )_________  __/__  /________      __
____  /| |_  /__  ___/_  /_ __  /_  __ \_ | /| / /
___  ___ |  / _  /   _  __/ _  / / /_/ /_ |/ |/ /
 _/_/  |_/_/  /_/    /_/    /_/  \____/____/|__/
[2021-02-13 12:25:40,526] {scheduler_job.py:1247} INFO - Starting the scheduler
[2021-02-13 12:25:40,526] {scheduler_job.py:1252} INFO - Processing each file at most -1 times
....

$ ctrl + c
$ nohup airflow scheduler &
$ airflow webserver
....



```

##### Localhost :8080

go to `http://localhost:8080` in your browser 



#### Work with provided DAGs



