# orders_controller.py
from src.entities.order import Order
from src.entities.menu import Menu
from src.schema.delete_user_schema import DeleteItemSchema, DeleteOrderSchema
from src.schema.post_user_schema import PostUserSchema
from src.schema.put_user_schema import PutUserSchema

def controller_get_menu():
    return Menu.get_menu()

def controller_get_menu_by_category(category: str):
    return Menu.get_by_category(category=category)

def controller_get_menu_by_name(name: str):
    return Menu.get_by_name(name=name)

def controller_create_order(data: PostUserSchema):
    Order(table_number=data.table_number, main_course=data.main_course, drink=data.drink, starter=data.starter)
    return data

def controller_get_order(table_number: int = None):
    return Order.get_order(table_number=table_number)

def controller_update_order(data: PutUserSchema):
    return Order.put_order(table_number=data.table_number, item_id=data.item_id, new_main_course=data.new_main_course, new_drink=data.new_drink, new_starter=data.new_starter)

def controller_delete_order(data: DeleteOrderSchema):
    return Order.delete_order(table_number=data.table_number)

def controller_delete_item(data: DeleteItemSchema):
    return Order.delete_item(table_number=data.table_number, item_id=data.item_id)
