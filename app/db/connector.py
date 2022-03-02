from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure

from app.config import MONGO_DB, MONGO_HOST, MONGO_PASSWORD, MONGO_PORT, MONGO_USER
from app.crud.employees import employees_crud


class MongoConnector:
    def __init__(self):

        self.db = None
        self.client = None

    async def connect(self):
        self.client = AsyncIOMotorClient(
            username=MONGO_USER,
            password=MONGO_PASSWORD,
            host=MONGO_HOST,
            port=MONGO_PORT,
            connect=True,
        )
        # Perform fast test command execution to check connection
        try:
            await self.client.admin.command("ismaster")
        except ConnectionFailure:
            raise ConnectionFailure("MongoDB server connection timeout")

        self.db = self.client[MONGO_DB]
        employees_crud.collection = self.db.employees

        if not await self.db.employees.count_documents({}):
            # TODO: по-хорошему, лучше бы так данные в базу не загружать, а делать это в каком-то специальном месте
            await self.fill_db()

    async def fill_db(self):
        import json

        data = json.load(open("../employees.json"))
        self.db.employees.insert_many(data)

    async def disconnect(self):
        self.client.close()
        self.client = None
        self.db = None


mongo_connector = MongoConnector()
