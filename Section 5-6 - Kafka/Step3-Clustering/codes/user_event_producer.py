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