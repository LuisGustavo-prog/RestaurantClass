from app.src.routes.routes import app
from app.src.page.page import home
from fastapi.responses import HTMLResponse

@app.get('/', response_class=HTMLResponse)
def main():
    return home()
