import uuid
from src.database.connection import db

def generate_id():
    return str(uuid.uuid4())
    
def generate_waiter_id():
    last_waiter = db.waiter.find_one(sort=[('waiter_id', -1)])

    if last_waiter is None:
        return 1
    
    return last_waiter['waiter_id'] + 1
    