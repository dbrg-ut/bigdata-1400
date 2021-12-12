

1. Check out  `stock-exchange-v4.py`

 

   #### in namenode container 
```bash
hadoop fs -mkdir -p  /data/data_lake/stock/fa_year=\"1399\"
```



   Airflow Admin : 
    -  create webhdfs_default Connection Variable -> **type** : hdfs , **host** : namenode , **port** : 9870  
    -  create fs_temp variable -> extra : {"path": "/tmp"}



   





 

