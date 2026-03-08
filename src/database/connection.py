from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = MongoClient(os.getenv('MONGO_URL'))
    client.admin.command('ping')

    db = client['restaurant']

    orders_collection = db['orders']
    menu_collection = db['menu']
    waiter_collection = db['waiters']
except Exception as e:
    print(f'Error: Error connecting to the database. {e}')
    raise
