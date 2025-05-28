import motor.motor_asyncio
from django.conf import settings
from beanie import init_beanie
from subscription.mongo_models.address import Address

async def init_db():
  client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
  db = client[settings.MONGO_DEV_DB_NAME]
  await init_beanie(database=db, document_models=[Address])
  print("=== BEANIE INITIALIZED ===")
