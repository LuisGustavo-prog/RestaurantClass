from fastapi import APIRouter
from src.schema.delete_user_schema import DeleteItemSchema, DeleteOrderSchema
from src.schema.post_user_schema import PostUserSchema 
from src.schema.put_user_schema import PutUserSchema
from src.controllers.orders_controller import (
    controller_create_order,
    controller_get_order,
    controller_get_all_order,
    controller_update_order,
    controller_delete_order,
    controller_delete_item
)

orders = APIRouter(tags=["Orders"])

@orders.post('/orders/')
def create_order(data: PostUserSchema):
    return controller_create_order(data)

@orders.get('/orders/')
def get_order(table_number: int = None):
    return controller_get_order(table_number=table_number)

@orders.get('/orders/all/')
def get_all_orders():
    return controller_get_all_order()

@orders.put('/orders/')
def update_order(data: PutUserSchema):
    return controller_update_order(data)

@orders.delete('/orders/')
def delete_order(data: DeleteOrderSchema):
    return controller_delete_order(data)

@orders.delete('/orders/item/')
def delete_item(data: DeleteItemSchema):
    return controller_delete_item(data)
