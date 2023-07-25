#!/usr/bin/python3

from datetime import datetime
from time import sleep
from kafka import KafkaProducer
import random
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))

while True:
    data = dict()
    data['sensor'] = 'LDR12345'
    data['reading'] = random.randint(0, 80)
    data['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    producer.send(topic='iot', value=data)
    print('sent: ', data)
    sleep(1)
