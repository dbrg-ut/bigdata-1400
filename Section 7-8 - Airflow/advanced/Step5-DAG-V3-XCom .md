#### Working With Sensors & Connection



1. Check out  `stock-exchange-v3.py`

   ```python
   def preprocess_convert_to_csv(**kwargs) :
       ti = kwargs['ti']
    	....
       ti.xcom_push(key='fa_year', value=today.year)
   
   
       
   
   ```
   
   

2. Run the `Stock-Exchange-V3 DAG. 

3. Check `XCom` Variables in Admin Panel

4. [Macros reference — Airflow Documentation (apache.org)](https://airflow.apache.org/docs/apache-airflow/stable/macros-ref.html)

   

   

   

   
   
    

