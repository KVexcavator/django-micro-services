# subscription/mongo_models/address.py
from beanie import Document
from pydantic import EmailStr, Field
from datetime import datetime
from bson import ObjectId
from beanie import PydanticObjectId

class Address(Document):
    name: str = Field(..., max_length=120)
    address: str = Field(..., max_length=120)
    postalcode: str = Field(..., max_length=20)
    city: str = Field(..., max_length=120)
    country: str = Field(..., max_length=80)
    email: EmailStr
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "addresses"
