from fastapi import FastAPI
from db import r as db
import json, calculate
from pydantic import BaseModel

app = FastAPI()

class location(BaseModel): 
    X_COORD: str
    Y_COORD: str


@app.get("/")
def root():
    return {"message": "Hello World 👋"}

@app.get("/culture")
def getCulturalEventInfo():
    data = db.get('getCulturalEventInfo')
    return json.loads(data)

@app.get("/culturalSpaceInfoList")
def stadiumScheduleInfo():
    data = db.get('culturalSpaceInfo')
    return json.loads(data)

@app.post("/stadiumScheduleLoactionCal")
async def stadiumScheduleLoactionCal(item: location):
    data = db.get('culturalSpaceInfo')["culturalSpaceInfo"]["row"]
    OWN_X_COORD = location.X_COORD
    OWN_Y_COORD = location.Y_COORD
    nearest_events = calculate.find_nearest_events(OWN_X_COORD, OWN_Y_COORD, data, '3')
    return nearest_events