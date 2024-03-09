from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    # discount: str
    image: str

