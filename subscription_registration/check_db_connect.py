import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subscription_registration.settings")
django.setup()

import motor.motor_asyncio
from django.conf import settings
import asyncio

MONGO_URI = settings.MONGO_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[settings.MONGO_DEV_DB_NAME]

async def check_connection():
  try:
    result = await client.admin.command('ping')
    print("MongoDB connection is OK:", result)
  except Exception as e:
    print("Failed to connect to MongoDB:", str(e))

if __name__ == "__main__":
  asyncio.run(check_connection())

# docker exec -it sub_reg bash
# python check_db_connect.py
