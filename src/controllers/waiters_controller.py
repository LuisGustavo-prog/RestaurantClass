from src.entities.waiter import Waiter
from src.schema.waiter_schema import (
    CreateWaiterSchema,
    UpdateWaiterSchema,
    DeleteWaiterSchema
)

def controller_create_waiter(data: CreateWaiterSchema):
    Waiter(name=data.name, cpf=data.cpf, wage=data.wage, email=data.email, phone_number=data.phone_number)

    return {'error': False, 'message': 'Waiter created successfully.'}

def controller_get_all_waiters():
    return Waiter.get_all_waiters()

def controller_get_waiters_by_id(waiter_id: int):
    return Waiter.get_waiters_by_id(waiter_id=waiter_id)

def controller_update_waiter(data: UpdateWaiterSchema):
    return Waiter.update_waiter(waiter_id=data.waiter_id, new_name=data.new_name, new_wage=data.new_wage, new_email=data.new_email, new_phone_number=data.new_phone_number)

def controller_delete_waiter(data: DeleteWaiterSchema):
    return Waiter.delete_waiter(waiter_id=data.waiter_id)
