#### Working With Official Airflow Docker-Compose File

[Running Airflow in Docker — Airflow Documentation (apache.org)](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)

*setup an airflow cluster using provided docker file by apache foundation.*

**we made these changes :** 

- 2 workers 

- mount `dags` and `plugins` folder to appropriate target address.

  

**looking around :** 


0. **Check the docker-compose file** 

1. **to setup the cluster , run :**


```bash
$ docker-compose -f .\docker-compose-apache.yml up
```

2. after the cluster getting up and ready, **go to Airflow UI** : `localhost:8080`  

   user & password : `airflow`

3. **Checking Workers**

  - Check  the DAG Python File . (*Constants, Scheduler Interval,  Main task*)
  - Enable the DAG
  - Trigger the Dag and check the log file  
  - Locate the `downloaded file`  using  ` docker exec -it docker_airflow-worker1_1 bash`. 
  - Check out the task by using Celery Flower UI : `localhost:5555` (Concepts:  *process/concurrency/broker*)
  - Trigger the Dag **Multiple Times** and check the Worker Status  

4. **Append random Number to Excel Files ** *(for testing purposes)*
- change the `Bash Operator` to run this command :

```bash
$ curl --retry 10 --output /tmp/daily_trades_$(echo $RANDOM).xls -L -H "User-Agent:Chrome/61.0" --compressed "http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=0"
```

- Trigger the Dag **Multiple Times** and check the `/tmp` to verify
- *Tasks Must Be Idempotent!*
- revert changes!

5. **Python Code Outside the functions**

- add these lines to the DAG file (*after import  section*)

  ```python
  import time
  timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
  f= open(f"/tmp/'{timestr}.txt",'w')
  f.close()
  ```

- go to scheduler container and check the `/tmp` folder 

- *Be careful when you run code outside the Airflow Operators*

- revert changes!

6. **Using Run Time Configs**

- change the bash operator to this one : 

   ```python
    bash_command='curl --retry 10 --output  {0} -L -H "User-Agent:Chrome/61.0" --compressed "http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d={{{{dag_run.conf.get(\'day\',\'0\')}}}}"'.format( path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, '{{dag_run.conf.get("day","current_day")}}', EXCEL_FILE_EXT))),    

   ```

- trigger the **dag** and enter this json when it promptes you : 

```json
{
"day":"1399-11-20"
}
```

- check the task log to verify everything is OK!
- there is [a lot more Macros there](https://airflow.apache.org/docs/apache-airflow/1.10.9/macros.html)!







