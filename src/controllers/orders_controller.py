# orders_controller.py
from src.entities.order import Order
from src.schema.delete_user_schema import DeleteItemSchema, DeleteOrderSchema
from src.schema.post_user_schema import PostUserSchema
from src.schema.put_user_schema import PutUserSchema

def controller_create_order(data: PostUserSchema):
    try:
        Order(table_number=data.table_number, waiter_id=data.waiter_id, main_course=data.main_course, drink=data.drink, starter=data.starter)
        return data
    except ValueError as e:
        return {'error': True, 'message': str(e)}

def controller_get_order(table_number: int = None):
    return Order.get_order(table_number=table_number)

def controller_get_all_order():
    return Order.get_all_orders()

def controller_update_order(data: PutUserSchema):
    try:
        return Order.put_order(table_number=data.table_number, item_id=data.item_id, new_main_course=data.new_main_course, new_drink=data.new_drink, new_starter=data.new_starter)
    except ValueError as e:
        return {'error': True, 'message': str(e)}

def controller_delete_order(data: DeleteOrderSchema):
    return Order.delete_order(table_number=data.table_number)

def controller_delete_item(data: DeleteItemSchema):
    return Order.delete_item(table_number=data.table_number, item_id=data.item_id)
