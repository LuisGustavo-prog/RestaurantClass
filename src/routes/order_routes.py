from src.app import app
from src.schema.delete_user_schema import DeleteItemSchema, DeleteOrderSchema
from src.schema.post_user_schema import PostUserSchema 
from src.schema.put_user_schema import PutUserSchema
from src.controllers.orders_controller import (
    controller_get_menu,
    controller_get_menu_by_category,
    controller_get_menu_by_name,
    controller_create_order,
    controller_get_order,
    controller_update_order,
    controller_delete_order,
    controller_delete_item
)

@app.get('/menu/')
def get_menu():
    return controller_get_menu()

@app.get('/menu/category/')
def get_menu_by_category(category: str):
    return controller_get_menu_by_category(category=category)

@app.get('/menu/name/')
def get_menu_by_name(name: str):
    return controller_get_menu_by_name(name=name)

@app.post('/orders/')
def create_order(data: PostUserSchema):
    return controller_create_order(data)

@app.get('/orders/')
def get_order(table_number: int = None):
    return controller_get_order(table_number=table_number)

@app.put('/orders/')
def update_order(data: PutUserSchema):
    return controller_update_order(data)

@app.delete('/orders/')
def delete_order(data: DeleteOrderSchema):
    return controller_delete_order(data)

@app.delete('/orders/item/')
def delete_item(data: DeleteItemSchema):
    return controller_delete_item(data)
