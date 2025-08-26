from kafka import KafkaProducer


import json

class Push_kafka:

    def __init__(self):
        pass

    def connect(self):
        self.producer = KafkaProducer(bootstrap_servers = 'localhost:9092',
                                    #   value_serializer = lambda x: json.dumps(x).encode('utf-8')
                                      )

    def send_by_topic(self,topic,arr):
        for i in range(1):
            dic = {}
            dic['data'] = arr.data[i]
            dic['target_name'] = arr.target_names[arr.target[i]]
            self.producer.send(topic,json.dumps(dic).encode('utf-8'))

    def close(self):
        self.producer.close()
