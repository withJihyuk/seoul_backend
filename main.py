from fastapi import FastAPI
from db import r as db
import json

app = FastAPI()

origins = [
    "https://seoul.mya.ong",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    
