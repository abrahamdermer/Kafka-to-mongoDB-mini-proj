from kafka import KafkaProducer




class Push_kafka:

    def __init__(self):
        pass

    def connect(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def send_by_topic(self,topic,arr):
        for message in arr:
            self.producer.send(topic, message.encode('utf-8')) 

    def close(self):
        self.producer.close()
