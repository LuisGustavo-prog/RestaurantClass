from src.entities.order import Order
from src.schema.delete_user_schema import DeleteUserSchema
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


@app.post('/post/')
def post_command(data: PostUserSchema): 
    Order(table_number=data.table_number, main_course=data.main_course, drink=data.drink, starter=data.starter)

    return data

@app.get('/get/')
def get_command(table_number: int = None):
    return Order.get_order(table_number=table_number)

@app.put('/put/')
def put_command(data: PutUserSchema):
    result_put = Order.put_order(table=data.table, item_number=data.item, new_main_course=data.new_main_course, new_drink=data.new_drink, new_starter=data.new_starter)

    return result_put

@app.delete('/delete/')
def delete_command(data: DeleteUserSchema):
    return Order.delete_order(table_number=data.table_number, item_number=data.item_number, type_of_choice=data.type_of_choice)
