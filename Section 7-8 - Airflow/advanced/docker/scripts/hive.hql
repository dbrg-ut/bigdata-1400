CREATE EXTERNAL TABLE IF NOT EXISTS Stock_Exchange_Daily_Partitioned(
symbol STRING,
full_name STRING,
quantity BIGINT,
volume BIGINT,
value BIGINT,
yesterday_qnt BIGINT,
first_order_value INT,
last_order_value INT,
last_order_value_change FLOAT,
last_order_value_change_percent FLOAT,
close_price INT,
close_price_change FLOAT,
close_price_change_percent FLOAT,
min_price INT,
max_price INT,
EPS INT,
PE FLOAT,
buy_quantity INT,
buy_volume INT,
buy_price INT,
sell_volume INT,
sell_price INT,
sell_quantity INT,
fa_date STRING,
en_date DATE
) 
COMMENT 'Daily Trades Of Iranian Stocks - Aggregated By TSETMC'
PARTITIONED BY (fa_year STRING)
row format delimited fields terminated by ','
STORED AS TEXTFILE LOCATION '/data/data_lake/stock'
TBLPROPERTIES ('skip.header.line.count'='1');


ALTER TABLE default.stock_exchange_daily_partitioned ADD PARTITION (fa_year="1399") LOCATION '/data/data_lake/stock/fa_year="1399"';
ALTER TABLE default.stock_exchange_daily_partitioned ADD PARTITION (fa_year="1399") LOCATION '/data/data_lake/stock/fa_year="1400"';



select count(*) 
from stock_exchange_daily_partitioned ;




