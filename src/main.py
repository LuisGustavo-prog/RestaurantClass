from src.routes.routes import app
from src.templates.page import home
from fastapi.responses import HTMLResponse

@app.get('/', response_class=HTMLResponse)
def main():
    return home()

# Comando para rodar o servidor local: python -m uvicorn src.main:app --reload
