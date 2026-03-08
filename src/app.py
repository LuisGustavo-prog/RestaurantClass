from fastapi import FastAPI
from src.routes.waiters_routes import waiter
from src.routes.order_routes import orders
from src.routes.menu_routes import menu

app = FastAPI(
    title="API Comanda - Sistema de Pedidos",
    description="API REST para gerenciamento de comandas e pedidos de restaurante",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(waiter)

app.include_router(menu)

app.include_router(orders)
