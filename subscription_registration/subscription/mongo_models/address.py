# subscription/mongo_models/address.py
from beanie import Document
from pydantic import EmailStr, Field
from datetime import datetime
from bson import ObjectId
from beanie import PydanticObjectId

class Address(Document):
    name: str = Field(..., max_length=120)
    address: str
    postalcode: str
    city: str
    country: str
    email: EmailStr
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "addresses"
