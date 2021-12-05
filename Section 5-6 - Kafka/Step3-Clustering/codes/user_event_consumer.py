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