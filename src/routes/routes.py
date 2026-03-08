from src.entities.order import Order
from src.schema.delete_user_schema import DeleteItemSchema, DeleteOrderSchema
from src.schema.put_user_schema import PutUserSchema
from src.schema.post_user_schema import PostUserSchema 
from fastapi import FastAPI
from src.entities.menu import Menu

app = FastAPI(
    title="API Comanda - Sistema de Pedidos",
    description="API REST para gerenciamento de comandas e pedidos de restaurante",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get('/menu/')
def get_menu():
    return Menu.get_menu()

@app.get('/menu/category/')
def get_menu_by_category(category: str):
    return Menu.get_by_category(category=category)

@app.get('/menu/name/')
def get_menu_by_name(name: str):
    return Menu.get_by_name(name=name)

@app.post('/orders/')
def create_order(data: PostUserSchema): 
    Order(table_number=data.table_number, main_course=data.main_course, drink=data.drink, starter=data.starter)
    return data

@app.get('/orders/')
def get_order(table_number: int = None):
    return Order.get_order(table_number=table_number)

@app.put('/orders/')
def update_order(data: PutUserSchema):
    return Order.put_order(table_number=data.table_number, item_id=data.item_id, new_main_course=data.new_main_course, new_drink=data.new_drink, new_starter=data.new_starter)

@app.delete('/orders/')
def delete_order(data: DeleteOrderSchema):
    return Order.delete_order(table_number=data.table_number)

@app.delete('/orders/item/')
def delete_item(data: DeleteItemSchema):
    return Order.delete_item(table_number=data.table_number, item_id=data.item_id)