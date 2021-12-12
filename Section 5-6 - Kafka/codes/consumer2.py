import json 
from kafka import KafkaConsumer

print("Connecting to consumer ...")
consumer = KafkaConsumer(
    'numbers',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group2',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
 print(f"Partition:{message.partition}\tOffset:{message.offset}\tKey:{message.key}\tValue:{message.value}")
 # print(f"{message}")

