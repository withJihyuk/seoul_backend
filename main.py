from fastapi import FastAPI
from db import r as db
import json, calculate
from pydantic import BaseModel

app = FastAPI()

class location(BaseModel): 
    X_COORD: float
    Y_COORD: float


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
    data = json.loads(db.get('culturalSpaceInfo').decode('utf-8'))
    OWN_X_COORD = item.X_COORD
    OWN_Y_COORD = item.Y_COORD
    nearest_events = calculate.find_nearest_events(OWN_X_COORD, OWN_Y_COORD, data, 3)
    return nearest_events