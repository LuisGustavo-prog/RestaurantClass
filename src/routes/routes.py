from src.models.order import Order
from src.schema.delete_user_schema import DeleteUserSchema
from src.schema.put_user_schema import PutUserSchema
from src.schema.post_user_schema import PostUserSchema 
from fastapi import FastAPI

app = FastAPI(
    title="API Comanda - Sistema de Pedidos",
    description="API REST para gerenciamento de comandas e pedidos de restaurante",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.post('/post/')
def post_command(data: PostUserSchema): # Mudar para schema
    """
    Cria um novo pedido para uma mesa.
    
    Args:
        table_number: Número da mesa
        main_course: Prato principal (opcional)
        drink: Bebida (opcional)
        salad: Salada (opcional)
    
    Returns:
        dict: Dados do pedido criado
    """
    Order(table_number=data.table_number, main_course=data.main_course, drink=data.drink, salad=data.salad)

    return data

@app.get('/get/')
def get_command(table: int = None, type_of_choice: str = 'all'):
    """
    Busca pedidos do sistema.
    
    Args:
        table: Número da mesa para busca específica (opcional)
        type_of_choice: Tipo de busca - 'all' para todos os pedidos ou 'specific' para um pedido específico
    
    Returns:
        str: Dados do(s) pedido(s) encontrado(s)
    """
    return Order.get_order(table=table, type_of_choice=type_of_choice)

@app.put('/put/')
def put_command(data: PutUserSchema):
    """
    Atualiza um item específico de um pedido.
    
    Args:
        table: Número da mesa
        item: Número do item a ser atualizado
        new_main_course: Novo prato principal (opcional)
        new_drink: Nova bebida (opcional)
        new_salad: Nova salada (opcional)
    
    Returns:
        dict: Dados do item atualizado
    """
    result_put = Order.put_order(table=data.table, item_number=data.item, new_main_course=data.new_main_course, new_drink=data.new_drink, new_salad=data.new_salad)

    return result_put

@app.delete('/delete/')
def delete_command(data: DeleteUserSchema):
    """
    Deleta pedidos do sistema.
    
    Args:
        table_number: Número da mesa para deletar (opcional)
        item_number: Número do item específico para deletar (opcional)
        type_of_choice: Tipo de deleção - 'all' para deletar todos os pedidos ou 'specific' para deletar pedido específico
    
    Returns:
        str: Mensagem de confirmação da deleção
    """
    return Order.delete_order(table_number=data.table_number, item_number=data.item_number, type_of_choice=data.type_of_choice)
