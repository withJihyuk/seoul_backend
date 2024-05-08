from fastapi import FastAPI
from db import r as db
import json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World 👋"}

@app.get("/culture")
def getCulturalEventInfo():
    data = db.get('getCulturalEventInfo')
    return json.loads(data)

@app.get("/sport")
def stadiumScheduleInfo():
    data = db.get('stadiumScheduleInfo')
    return json.loads(data)