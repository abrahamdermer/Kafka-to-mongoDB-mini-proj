from fastapi import FastAPI
from dal import DAL


app = FastAPI()
dal = DAL()

@app.get("/")
def read_root():
    return {"status":True}
    
@app.get("/interesting")
def read_root():
    rec = {"news":dal.get_all_tata_from_colume("interesting")}
    return rec
    
@app.get("/not-interesting")
def read_root():
    rec = {"news":dal.get_all_tata_from_colume("not_interesting")}
    return rec
    