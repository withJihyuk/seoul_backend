from db import r as db
import requests, os, json
import datetime, pytz

KST = pytz.timezone('Asia/Seoul')
now = datetime.datetime.now(tz=KST)

# 행사 데이터
url= f"http://openapi.seoul.go.kr:8088/{os.environ['API_KEY']}/json/culturalEventInfo/1/100/%20/%20/{now.strftime("%Y-%m")}"
res = requests.get(url)
data = res.json()

# 데이터를 캐시화
db.set('getCulturalEventInfo', json.dumps(data))