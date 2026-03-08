from fastapi import FastAPI
from src.routes.waiters_routes import waiter

app = FastAPI(
    title="API Comanda - Sistema de Pedidos",
    description="API REST para gerenciamento de comandas e pedidos de restaurante",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(waiter)
