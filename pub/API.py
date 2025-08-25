from fastapi import FastAPI

from pull_news import News
from push_kafka import Push_kafka

app = FastAPI()
news = News()
kap = Push_kafka()
kap.connect()

@app.get("/")
def read_root():
    new_news = news.get_news()
    kap.send_by_topic('interesting',new_news['newsgroups_interesting']) 
    kap.send_by_topic('not_interesting',new_news['newsgroups_not_interesting'])
    return {"status":True}
    