from fastapi import APIRouter

waiter = APIRouter()

@waiter.post('/waiters/')
def create_waiter():
    pass

@waiter.get('/waiters/')
def get_waiters():
    pass

@waiter.put('/waiters/')
def update_waiter():
    pass

@waiter.delete('/waiters/')
def delete_waiter():
    pass

