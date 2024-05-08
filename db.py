import redis
import os

print(os.environ['DB_URL'])
r = redis.Redis(
  host= f"{os.environ['DB_URL']}",
  port=34888,
  password=os.environ['DB_PASSWORD'],
  ssl=True
)