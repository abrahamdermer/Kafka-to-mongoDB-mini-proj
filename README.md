Three folders for three parts:
The "pub" folder receives news and sends it to Kafka. It is activated in the API.PY file.
The "sub" folder contains 2 listeners that pull and put into the cloud. You need to run the files sub1.py and sub2.py.
The client folder raises a server that returns the news according to routes. You need to run the API.py.


kafka in - 'localhost:9092'
monngo in - "mongodb://localhost:27000/"  ** NOT 27017 ** 

pub in port - 8000
client in port - 8080