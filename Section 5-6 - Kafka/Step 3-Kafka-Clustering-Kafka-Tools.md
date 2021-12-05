#### Setup Kafka Cluster with Docker

- we will use Confluent community docker images.

  ```bash
  $ docker-compose  -f .\docker-compose-cluster.yml up -d
  $ $ docker-compose  -f .\docker-compose-cluster.yml ps
  ```

> listeners - Comma-separated list of URIs we will listen on and their protocols. `listeners` is what the broker will use to create server sockets.
>
> `advertised.listeners` is what clients will use to connect to the brokers.  Listeners to publish to ZooKeeper for clients to use.
>
> 

#### Set Hostnames in wsl/windows

- edit `/etc/hosts` in WSL and add the following lines :

```bash
sudo nano /etc/hosts
...
127.0.0.1	kafka1
127.0.0.1	kafka2
127.0.0.1	kafka3
```

- open `notepad` as Administrator/ open `C:\Windows\System32\drivers\etc\hosts`  (select `All Files` filter to be able to see the `hosts` file) and add the above settings. (Check out that the `hosts` file is not `Read Only`)
- Run `ipconfig /flushdns` in powershell/cmd
- Run `ping kafka1` to confirm everything is OK.

#### Create `events_topic` Topic

- enter the kafka broker container. create a topic named `numbers`

```bash
$ docker exec -it kafka1 bash
$ kafka-topics --bootstrap-server kafka1:29092 --create  --topic events_topic  --partitions 4 --replication-factor 2
$ exit
$ wsl
$ kafkacat -b localhost:9091 -L -t events_topic
Metadata for events_topic (from broker -1: localhost:9093/bootstrap):
 3 brokers:
  broker 2 at kafka2:9092 (controller)
  broker 3 at kafka3:9092
  broker 1 at kafka1:9092
 1 topics:
  topic "events_topic" with 4 partitions:
    partition 0, leader 1, replicas: 1,2, isrs: 2,1
    partition 1, leader 2, replicas: 2,3, isrs: 3,2
    partition 2, leader 3, replicas: 3,1, isrs: 3,1
    partition 3, leader 1, replicas: 1,3, isrs: 3,1
    
$ kafkacat -b localhost:9093 -L -t events_topic
Metadata for events_topic (from broker -1: localhost:9095/bootstrap):
 3 brokers:
  broker 2 at kafka2:9092 (controller)
  broker 3 at kafka3:9092
  broker 1 at kafka1:9092
 1 topics:
  topic "events_topic" with 4 partitions:
    partition 0, leader 3, replicas: 3,2, isrs: 3,2
    partition 1, leader 1, replicas: 1,3, isrs: 1,3
    partition 2, leader 1, replicas: 2,1, isrs: 1,2
    partition 3, leader 1, replicas: 3,1, isrs: 1,3    
    
```

#### Produce Some Messages

-  Go to Section15 folder. activate `.venv` and install required libraries.

  ```bash
  $ source .venv/bin/activate
  $ cd Step3-Clustering
  $ pip3 install -r codes/requirements.txt
  ```

- run the `producer.py` to generate some simple messages.

  ```bash
  $ python3 ./codes/user_event_producer.py
  Event Created : fce097bf-152f-46ab-91e4-11d222b814df
  Event Created : 034e2569-3bc1-465d-9783-0e6e6c256e50
  Event Created : 251f113c-1287-4958-99cf-9998add7bce2
  ```

- **producer code :**

  ```python
  from datetime import datetime
  import json
  from kafka import KafkaProducer
  import random
  import time
  import uuid
  
  EVENT_TYPE_LIST = ['buy', 'sell', 'click', 'hover', 'idle_5']
  
  producer = KafkaProducer(
     value_serializer=lambda msg: json.dumps(msg).encode('utf-8'), # we serialize our data to json for efficent transfer
     bootstrap_servers=['kafka1:9091','kafka2:9092','kafka3:9093'],
     key_serializer=str.encode)
  
  TOPIC_NAME = 'events_topic'
  
  
  def _produce_event():
      """
      Function to produce events
      """
      # UUID produces a universally unique identifier
      return {
          'event_id': str(uuid.uuid4()),
          'event_datetime': datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
          'event_type': random.choice(EVENT_TYPE_LIST)
      }
  
  def send_events():
      while(True):
          data = _produce_event()
          time.sleep(3) # simulate some processing logic
          producer.send(TOPIC_NAME, value=data, key=data['event_id'])
          print(f"Event Created : {data['event_id']}")
  
  if __name__ == '__main__':
      send_events()
  ```

  

- checkout the `events_topic`  using `kafkacat`

```bash
$ wsl
$  kafkacat -b kafka1:9091 -C -t events_topic
{"event_id": "b4065464-f3b4-4349-a5e0-27e12f90e772", "event_datetime": "2021-06-27-20-13-41", "event_type": "idle_5"}
{"event_id": "2782d6f6-1adf-4043-9eda-5274cddd74db", "event_datetime": "2021-06-27-20-13-56", "event_type": "hover"}
....

```



- Open another console and activate the `venv`

- Consume Messages with `user_event_consumer.py`

  - run the consumer script :

  ```bash
  $ python3 ./codes/user_event_consumer.py
  ```

  - consumer code :

  ```python
  import json
  from kafka import KafkaConsumer
  
  TOPIC_NAME = 'events_topic'
  
  consumer = KafkaConsumer(
      TOPIC_NAME,
      auto_offset_reset='earliest', # where to start reading the messages at
      group_id='event-collector-group-1', # consumer group id
      bootstrap_servers=['kafka1:9091','kafka2:9092','kafka3:9093'],
      value_deserializer=lambda m: json.loads(m.decode('utf-8')) ,# we deserialize our data from json
      security_protocol= 'PLAINTEXT'
  )
  
  def consume_events():
      for message in consumer:
          # any custom logic you need
          print(f"Partition:{message.partition}\tOffset:{message.offset}\tKey:{message.key}\tValue:{message.value}")
  
  if __name__ == '__main__':
      print("Consumer Started ...")
      consume_events()
  ```

- Stop `Kafka1`  and check out the `Producer/Consumer/Topic`

```bash
$ docker-compose -f .\docker-compose-cluster2.yml stop kafka1
$ kafkacat -b kafka3:9093 -L -t events_topic

```

- Stop `Kafka2`  and check out the `Producer/Consumer/Topic`

```bash
$ docker-compose -f .\docker-compose-cluster2.yml stop kafka1
$ kafkacat -b kafka3:9093 -L -t events_topic
```

- start Kafka2
- start Kafka1

#### Using Offset Explorer to Visually Mange the Kafka  Cluster

- download & install [OffsetExplorer](https://www.kafkatool.com/) (formerly known as KafkaTools)
- add cluster and view the `Topics/Brokers/Consumers....`

