from fastapi import APIRouter
# from src.controllers.waiters_controller import (
#     controller_create_waiter,
#     controller_get_waiters,
#     controller_update_waiter,
#     controller_delete_waiter
# )
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

