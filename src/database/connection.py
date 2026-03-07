from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = MongoClient(os.getenv('MONGO_URL'))
    client.admin.command('ping')

    db = client['restaurant']

    orders_collection = db["orders"]
except Exception as e:
    print(f'Error: Error connecting to the database. {e}')
