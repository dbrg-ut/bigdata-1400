#### Setup Kafka Cluster with Docker

- we will use Confluent community docker images.

  ```bash
  $ docker-compose  -f .\docker-compose.yml up -d
  $ docker-compose logs kafka | grep -i started
  ```

  

#### Install KafkaCat

- a general purpose cli utility for working with kafka

```bash
$ wsl
$ sudo apt update
$ sudo apt install kafkacat
$ kafkacat -b localhost:9092 -L
```

#### Create `Numbers` Topic

- enter the kafka broker container. create a topic named `numbers`

```bash
$ docker exec -it <KAFKA-CONTAINER_NAME_OR_ID> bash
$ kafka-topics --bootstrap-server localhost:9092 --create  --topic numbers  --partitions 4 --replication-factor 1
$ exit
$ kafkacat -b localhost:9092 -L -t numbers
Metadata for numbers (from broker -1: localhost:9092/bootstrap):
 1 brokers:
  broker 1 at kafka:9092 (controller)
 1 topics:
  topic "numbers" with 4 partitions:
    partition 0, leader 1, replicas: 1, isrs: 1
    partition 1, leader 1, replicas: 1, isrs: 1
    partition 2, leader 1, replicas: 1, isrs: 1
    partition 3, leader 1, replicas: 1, isrs: 1
    
```

#### Produce Some Numbers

- create a venv in `.venv` and activate it.

- run the `producer.py` to generate some simple messages.

  ```bash
  $ python3 ./codes/producer.py
  ```

- producer code :

  ```python
  from time import sleep
  from json import dumps
  from kafka import KafkaProducer
  
  producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
  
  for e in range(100):
   data = {'number' : e}
   producer.send('numbers', value=data)
   print(f"Sending data : {data}")
   sleep(5)
  
  ```

- key is not set in above code 

#### Consume Messages with `KafkaCat`

- open another console and use kafkacat to see the messages

```bash
$ kafkacat -C -b localhost:9092 -t numbers
```

- see every message in details (key is null?) :

```bash
$ kafkacat -C -b localhost:9092 -t numbers -J
```

- check out a specific partition

```bash
$ kafkacat -C -b localhost:9092 -t numbers -p 3 -J
```

#### Consume Messages with `consumer.py`

- run the consumer script :

```bash
$ python3 ./codes/consumer.py
```

- consumer code :

```python
import json 
from kafka import KafkaConsumer

print("Connecting to consumer ...")
consumer = KafkaConsumer(
    'numbers',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
 print(f"{message.value}")

```

#### Adding key to the Messages

- to be able to use kafka compaction, we need to specify a key for every message.
- change the producer key into :

```python
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'), key_serializer=str.encode )

for e in range(100):
 data = {'number' : e}
 producer.send('numbers', value=data, key= str(e))
 print(f"Sending data : {data}")
 sleep(5)
```

- check out the messages :

```bash
$ kafkacat -C -b localhost:9092 -t numbers -J
```

#### Delete All Messages

- we alter kafka topic retention time to purge all the messages 

```bash
$ docker exec -it <KAFKA-CONTAINER_NAME_OR_ID> bash
$ kafka-configs --bootstrap-server localhost:9092 --alter --entity-type topics --entity-name numbers --add-config retention.ms=1000
$ kafka-configs --bootstrap-server localhost:9092 --alter --entity-type topics --entity-name numbers --add-config retention.ms=604800000 

$ exit
$ kafkacat -C -b localhost:9092 -t numbers
% Reached end of topic numbers [0] at offset 64
% Reached end of topic numbers [1] at offset 39
% Reached end of topic numbers [2] at offset 42
% Reached end of topic numbers [3] at offset 55
```

#### Change Topic cleanup.policy into `compact`

- you can use `kafka-config` to modify the topic configurations :

```bash
$ docker exec -it <KAFKA-CONTAINER_NAME_OR_ID> bash
$ kafka-configs --bootstrap-server localhost:9092 --alter --entity-type topics --entity-name numbers --add-config cleanup.policy=compact

```

#### Consumer Group / Auto  Commit

- set message limit to 100 in `producer.py` 
- run `producer` and `consumer`
- stop & start the `consumer` 
  - ***is it consumes from the beginning?***

- set  `enable_auto_commit`  to False in `consumer.py`

```python
consumer = KafkaConsumer(
    'numbers',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=False,
     group_id='my-group',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))
```

- run consumer again ,  restart the `consumer`
  - ***is it consumes from the beginning?***

- set  `enable_auto_commit`  to True
- comment the line that contains `group_id`

```python
consumer = KafkaConsumer(
    'numbers',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     # group_id='my-group',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))
```

- run consumer again ,  restart the `consumer`
  - ***is it consumes from the beginning?***

##### Run Multiple Consumer 

- run 2 instances of `consumer.py`
- run 5 instances of `consumer.py`
  - **which instance is idle?**

#### Multiple Group

- change the group-id and repeat the test while the initial consumers are running.