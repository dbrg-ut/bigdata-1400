#### Working With Sensors & Connection



1. Check out  `stock-exchange-v1.py`

   ```python
   FileSensor(task_id="Waiting-Excel-File",
                                       fs_conn_id="fs_temp",
                                       filepath = path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, date.today().strftime("%Y_%m_%d"),EXCEL_FILE_EXT)),
                                       poke_interval = 10, # every 10 seconds,
                                       dag = dag
                                       )
   ```

   

2. Run the `Stock-Exchange-V1` DAG. 

3. Create a connection in Admin menu : 

   - name : fs_temp
   - connection type : file
   - extra : {"path": "/tmp"}

4. Clear recent Dag run 

5. Check the task

6. **What's wrong in this version of our DAG ?** 

    - if filename generated randomly ...
    - if multiple worker are running ...
    
7. for now : **Disable One Worker**

    