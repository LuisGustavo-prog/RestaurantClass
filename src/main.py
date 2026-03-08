from src.routes.order_routes import app
from src.templates.page import home
from fastapi.responses import HTMLResponse
from src.database.menu_data import populate_menu

populate_menu()

@app.get('/', response_class=HTMLResponse)
def main():
    return home()

# Comando para rodar o servidor local: python -m uvicorn src.main:app --reload
