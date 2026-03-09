from fastapi import APIRouter
from src.controllers.waiters_controller import (
    controller_create_waiter,
    controller_get_all_waiters,
    controller_get_waiters_by_id,
    controller_update_waiter,
    controller_delete_waiter
)
from src.schema.waiter_schema import (
    CreateWaiterSchema,
    UpdateWaiterSchema,
    DeleteWaiterSchema
)

waiter = APIRouter()

@waiter.post('/waiters/')
def create_waiter(data: CreateWaiterSchema):
    return controller_create_waiter(data)

@waiter.get('/waiters/all/')
def get_all_waiters():
    return controller_get_all_waiters()

@waiter.get('/waiters/')
def get_waiters_by_id(waiter_id: int):
    return controller_get_waiters_by_id(waiter_id=waiter_id)

@waiter.put('/waiters/')
def update_waiter(data: UpdateWaiterSchema):
    return controller_update_waiter(data)

@waiter.delete('/waiters/')
def delete_waiter(data: DeleteWaiterSchema):
    return controller_delete_waiter(data)
