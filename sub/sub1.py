import datetime

from kafka import KafkaConsumer
from push_to_mongo import Insertdb

db = Insertdb()


consumer = KafkaConsumer(
    'interesting',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  
    group_id='my-group'
)


for message in consumer:
    db.insert('interesting',
        {
        "message": message.value.decode('utf-8'),
        "time":datetime.datetime.now()
        })
    # print("message:", message.value.decode('utf-8'))
