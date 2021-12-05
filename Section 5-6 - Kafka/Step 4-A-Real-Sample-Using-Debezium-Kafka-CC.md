#### Prerequisites

- docker (`Docker Desktop` for windows)
- linux terminal (`WSL` in windows  with one linux distribution installed)
- `dbeaver` free universal database tools



##### References 

- [Tutorial :: Debezium Documentation - MySQL Version](https://debezium.io/documentation/reference/tutorial.html)
-  [Change Data Capture Using Debezium Kafka and Pg · Start Data Engineering](https://www.startdataengineering.com/post/change-data-capture-using-debezium-kafka-and-pg/)

#### Setup The Cluster

- run docker-compose to setup the cluster
- add `kafka` to `etc/host` and `hosts` file in windows .
  - `ping kafka` in both `Powershell/WSL` to verify it.

##### Data Base Structure

![Problem Definition](https://www.startdataengineering.com/images/change-data-capture-using-debezium-kafka-and-pg/problem_definition.png)

- How many times did a specific user change (also include delete) stock types ?

```sql
select count(*) from holding_pivot
where change_field = 'holding_stock'
and old_value <> new_value -- check if the stock type changed
and old_value is not null
and user_id = 'given user id';
```

- How many times did a specific user change stock quantity ?, same as above with one small change (left as an exercise for the reader)

- Between date 1 and date 2 what was the most commonly sold stock among all users?

```sql
select old_value from holding_pivot
where datetime_updated between 'given date 1' and 'given date 2'
and old_value <> new_value -- check if the stock type changed
and old_value is not null
group by old_value
order by count(*) desc
limit 1;
```

#### replication settings

```bash
$ docker exec -it postgres /bin/bash
$ cat /var/lib/postgresql/data/postgresql.conf

# CONNECTION
listen_addresses = '*'

# MODULES
shared_preload_libraries = 'decoderbufs,wal2json'

# REPLICATION
wal_level = logical             # minimal, archive, hot_standby, or logical (change requires restart)
max_wal_senders = 4             # max number of walsender processes (change requires restart)
#wal_keep_segments = 4          # in logfile segments, 16MB each; 0 disables
#wal_sender_timeout = 60s       # in milliseconds; 0 disables
max_replication_slots = 4       # max number of replication slots (change requires restart)

```

#### Create the Database and Primary Table 
- Use `DBeaver `

  ```sql
  create database data_engineer ;
  SET search_path TO data_engineer;
  CREATE SCHEMA bank;
  CREATE TABLE bank.holding (
      holding_id int,
      user_id int,
      holding_stock varchar(8),
      holding_quantity int,
      datetime_created timestamp,
      datetime_updated timestamp,
      primary key(holding_id)
  );
  ALTER TABLE bank.holding replica identity FULL;
  insert into bank.holding values (1000, 1, 'VFIAX', 10, now(), now());
  ```

 The above is standard sql, with the addition of `replica identity`. 

> This field has the option of being set as one of `DEFAULT, NOTHING, FULL and INDEX` which determines the amount of detailed information written to the WAL. We choose FULL to get all the before and after data for CRUD change events in our WAL, the `INDEX` option is the same as full but it also includes changes made to indexes in WAL which we do not require for our project’s objective. We also insert a row into the holding table



#### Connectors

- Check out this address to see the installed connectors - Kafka Connect 

  `http://localhost:8083/connectors`

  or try this  :

  ```bash
  $ curl -H "Accept:application/json" localhost:8083/connectors/
  []
  ```

  

- Set a new connector : 


```bash

$ curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{"name": "sde-connector", "config": {"connector.class": "io.debezium.connector.postgresql.PostgresConnector", "database.hostname": "postgres", "database.port": "5432", "database.user": "nikamooz", "database.password": "nikamooz", "database.dbname" : "data_engineer", "database.server.name": "bankserver1", "table.whitelist": "bank.holding"}}'

-----------
HTTP/1.1 201 Created
Date: Sat, 26 Jun 2021 21:52:07 GMT
Location: http://localhost:8083/connectors/sde-connector
Content-Type: application/json
Content-Length: 372
Server: Jetty(9.4.33.v20201020)

{"name":"sde-connector","config":{"connector.class":"io.debezium.connector.postgresql.PostgresConnector","database.hostname":"postgres","database.port":"5432","database.user":"nikamooz","database.password":"nikamooz","database.dbname":"data_engineer","database.server.name":"bankserver1","table.whitelist":"bank.holding","name":"sde-connector"},"tasks":[],"type":"source"}
```

- What We Done : 

```json
{
  "name": "sde-connector",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "postgres",
    "database.port": "5432",
    "database.user": "nikamooz",
    "database.password": "nikamooz",
    "database.dbname": "data_engineer",
    "database.server.name": "bankserver1",
    "table.whitelist": "bank.holding"
  }
}

```

- Check out  the connectors :

```bash
$ curl -H "Accept:application/json" localhost:8083/connectors/
["sde-connector"]

$ curl -H "Accept:application/json" localhost:8083/connectors/
{"name":"sde-connector","config":{"connector.class":"io.debezium.connector.postgresql.PostgresConnector","database.user":"nikamooz","database.dbname":"data_engineer","database.hostname":"postgres","database.password":"nikamooz","name":"sde-connector","database.server.name":"bankserver1","database.port":"5432","table.whitelist":"bank.holding"},"tasks":[{"connector":"sde-connector","task":0}],"type":"source"}
```



###### Consumer

```bash
$ wsl
$ kafkacat -b kafka:9092 -L 
$ kafkacat -b kafka:9092 -C -t "bankserver1.bank.holding"
$ kafkacat -b kafka:9092 -C -t "bankserver1.bank.holding" | jq

```



##### A Python Parser

- we write a file in home directory named `stream.py` to consume the `Payload`

  ```python
  #!/usr/bin/python3 -u
  # Note: the -u denotes unbuffered (i.e output straing to stdout without buffering data and then writing to stdout)
  
  import json
  import os
  import sys
  from datetime import datetime
  
  FIELDS_TO_PARSE = ['holding_stock', 'holding_quantity']
  
  
  def parse_create(payload_after, op_type):
      current_ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
      out_tuples = []
      for field_to_parse in FIELDS_TO_PARSE:
          out_tuples.append(
              (
                  payload_after.get('holding_id'),
                  payload_after.get('user_id'),
                  field_to_parse,
                  None,
                  payload_after.get(field_to_parse),
                  payload_after.get('datetime_created'),
                  None,
                  None,
                  current_ts,
                  op_type
              )
          )
  
      return out_tuples
  
  
  def parse_delete(payload_before, ts_ms, op_type):
      current_ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
      out_tuples = []
      for field_to_parse in FIELDS_TO_PARSE:
          out_tuples.append(
              (
                  payload_before.get('holding_id'),
                  payload_before.get('user_id'),
                  field_to_parse,
                  payload_before.get(field_to_parse),
                  None,
                  None,
                  ts_ms,
                  current_ts,
                  op_type
              )
          )
  
      return out_tuples
  
  
  def parse_update(payload, op_type):
      current_ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
      out_tuples = []
      for field_to_parse in FIELDS_TO_PARSE:
          out_tuples.append(
              (
                  payload.get('after', {}).get('holding_id'),
                  payload.get('after', {}).get('user_id'),
                  field_to_parse,
                  payload.get('before', {}).get(field_to_parse),
                  payload.get('after', {}).get(field_to_parse),
                  None,
                  payload.get('ts_ms'),
                  None,
                  current_ts,
                  op_type
              )
          )
  
      return out_tuples
  
  
  def parse_payload(input_raw_json):
      input_json = json.loads(input_raw_json)
      op_type = input_json.get('payload', {}).get('op')
      if op_type == 'c':
          return parse_create(
              input_json.get('payload', {}).get('after', {}),
              op_type
          )
      elif op_type == 'd':
          return parse_delete(
              input_json.get('payload', {}).get('before', {}),
              input_json.get('payload', {}).get('ts_ms', None),
              op_type
          )
      elif op_type == 'u':
          return parse_update(
              input_json.get('payload', {}),
              op_type
          )
      # no need to log read events
      return []
  
  
  for line in sys.stdin:
      # 1. reads line from unix pipe, assume only valid json come through
      # 2. parse the payload into a format we can use
      # 3. prints out the formatted data as a string to stdout
      # 4. the string is of format
      #    holding_id, user_id, change_field, old_value, new_value, datetime_created, datetime_updated, datetime_deleted, datetime_inserted
      data = parse_payload(line)
      for log in data:
          log_str = ','.join([str(elt) for elt in log])
          print(log_str, flush=True)
  ```

- make `stream.py` executable

  ```bash
  $ chmod +x stream.py
  ```
  
  
  
- run the consumer 

  ```bash
  $ kafkacat -b kafka:9092 -C -t "bankserver1.bank.holding" | python3 ./stream.py > ./holding_pivot.txt
  ```
  
- Execute Following SQL Scripts :

```sql
-- C
insert into bank.holding values (1001, 2, 'SP500', 1, now(), now());
insert into bank.holding values (1002, 3, 'SP500', 1, now(), now());

-- U
update bank.holding set holding_quantity = 100 where holding_id=1000;

-- d
delete from bank.holding where user_id = 3;
delete from bank.holding where user_id = 2;

-- c
insert into bank.holding values (1003, 3, 'VTSAX', 100, now(), now());

-- u
update bank.holding set holding_quantity = 10 where holding_id=1003;
```



- you can view the `Topics/Consumers/...` in `OffsetExplorer`

  



