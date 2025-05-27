# mongo/client.py
import motor.motor_asyncio
from django.conf import settings

MONGO_URI = settings.MONGO_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[settings.MONGO_DEV_DB_NAME]
