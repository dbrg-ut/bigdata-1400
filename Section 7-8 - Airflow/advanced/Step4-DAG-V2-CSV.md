#### Working With Sensors & Connection



1. Check out  `stock-exchange-v2.py`

   ```python
   def preprocess_convert_to_csv() :
       xlsx_file_path = path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, date.today().strftime("%Y_%m_%d"),EXCEL_FILE_EXT_XLSX))
       csv_file_path = path.join(EXCEL_FILE_PATH, "{0}_{1}.{2}".format(EXCEL_FILE_NAME, date.today().strftime("%Y_%m_%d"),EXCEL_FILE_EXT_CSV))
       df = pd.read_excel (xlsx_file_path, header=0, skiprows=2 , engine='openpyxl')
       today = jdatetime.date.today()
       df = df.assign(fa_date=today.strftime("%Y-%m-%d"))
       df = df.assign(en_date = date.today().isoformat())
       df = df.assign(fa_year = today.year)
       df.to_csv (csv_file_path, index = None, header=True,encoding="utf-8")
   
   ```

   

2. Run the `Stock-Exchange-V2` DAG. 

3. Check log (print command)

4. check `CSV` outside the container.

5. upcoming DAGs should be run alongside a hadoop cluster.

   

    
