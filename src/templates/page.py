from fastapi.responses import HTMLResponse
from src.routes.routes import app

@app.get('/', response_class=HTMLResponse)
def home():
    """
    Página inicial da API de gerenciamento de comandas.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API Comanda - Gestão de Pedidos</title>
        <style>
            * { 
                margin: 0; 
                padding: 0; 
                box-sizing: border-box; 
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #1e293b 100%);
                color: #fff;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                overflow: hidden;
            }
            
            /* Efeito de fundo animado */
            body::before {
                content: '';
                position: absolute;
                width: 200%;
                height: 200%;
                background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 1px, transparent 1px);
                background-size: 50px 50px;
                animation: backgroundMove 20s linear infinite;
                opacity: 0.3;
            }
            
            @keyframes backgroundMove {
                0% { transform: translate(0, 0); }
                100% { transform: translate(50px, 50px); }
            }
            
            .container {
                position: relative;
                z-index: 1;
                text-align: center;
                padding: 70px 50px;
                background: rgba(15, 23, 42, 0.7);
                border-radius: 35px;
                backdrop-filter: blur(20px);
                box-shadow: 
                    0 8px 32px rgba(0, 0, 0, 0.5),
                    inset 0 1px 0 rgba(99, 102, 241, 0.2),
                    0 0 100px rgba(99, 102, 241, 0.1);
                border: 1px solid rgba(99, 102, 241, 0.2);
                max-width: 800px;
                animation: fadeIn 0.8s ease-out;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .logo {
                font-size: 6.5em;
                margin-bottom: 20px;
                animation: float 3s ease-in-out infinite;
                filter: drop-shadow(0 0 20px rgba(99, 102, 241, 0.5));
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
            }
            
            h1 {
                font-size: 3.5em;
                margin-bottom: 20px;
                font-weight: 700;
                background: linear-gradient(135deg, #818cf8 0%, #c4b5fd 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                letter-spacing: -1px;
            }
            
            .subtitle {
                font-size: 1.35em;
                margin-bottom: 50px;
                color: #94a3b8;
                font-weight: 300;
                letter-spacing: 0.5px;
            }
            
            .info {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 25px;
                margin: 50px 0;
            }
            
            .info-box {
                background: rgba(30, 27, 75, 0.5);
                padding: 30px 25px;
                border-radius: 18px;
                transition: all 0.3s ease;
                border: 1px solid rgba(99, 102, 241, 0.2);
            }
            
            .info-box:hover {
                background: rgba(30, 27, 75, 0.8);
                transform: translateY(-5px);
                box-shadow: 0 10px 25px rgba(99, 102, 241, 0.3);
                border-color: rgba(99, 102, 241, 0.4);
            }
            
            .info-box strong {
                display: block;
                font-size: 0.95em;
                color: #94a3b8;
                margin-bottom: 12px;
                text-transform: uppercase;
                letter-spacing: 1.5px;
                font-weight: 600;
            }
            
            .info-box span {
                font-size: 1.8em;
                font-weight: 700;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 12px;
                color: #e0e7ff;
            }
            
            /* Framework centralizado */
            .framework-box {
                background: rgba(30, 27, 75, 0.5);
                padding: 30px 25px;
                border-radius: 18px;
                transition: all 0.3s ease;
                border: 1px solid rgba(99, 102, 241, 0.2);
                margin: 25px auto;
                max-width: 250px;
            }
            
            .framework-box:hover {
                background: rgba(30, 27, 75, 0.8);
                transform: translateY(-5px);
                box-shadow: 0 10px 25px rgba(99, 102, 241, 0.3);
                border-color: rgba(99, 102, 241, 0.4);
            }
            
            .framework-box strong {
                display: block;
                font-size: 0.95em;
                color: #94a3b8;
                margin-bottom: 12px;
                text-transform: uppercase;
                letter-spacing: 1.5px;
                font-weight: 600;
            }
            
            .framework-box span {
                font-size: 1.8em;
                font-weight: 700;
                color: #e0e7ff;
            }
            
            .buttons {
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 50px;
            }
            
            a {
                padding: 20px 40px;
                background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.2));
                color: #e0e7ff;
                text-decoration: none;
                border-radius: 15px;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                font-weight: 600;
                border: 2px solid rgba(99, 102, 241, 0.3);
                font-size: 1.1em;
                display: inline-flex;
                align-items: center;
                gap: 10px;
                position: relative;
                overflow: hidden;
            }
            
            a::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent);
                transition: left 0.5s;
            }
            
            a:hover::before {
                left: 100%;
            }
            
            a:hover {
                background: linear-gradient(135deg, rgba(99, 102, 241, 0.4), rgba(139, 92, 246, 0.4));
                transform: translateY(-3px);
                box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
                border-color: rgba(99, 102, 241, 0.6);
                color: #fff;
            }
            
            a:active {
                transform: translateY(-1px);
            }
            
            .status {
                display: inline-block;
                width: 14px;
                height: 14px;
                background: #10b981;
                border-radius: 50%;
                animation: pulse 2s ease-in-out infinite;
                box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
            }
            
            @keyframes pulse {
                0%, 100% { 
                    transform: scale(1);
                    box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
                }
                50% { 
                    transform: scale(1.1);
                    box-shadow: 0 0 0 10px rgba(16, 185, 129, 0);
                }
            }
            
            @media (max-width: 768px) {
                .container {
                    padding: 50px 30px;
                    margin: 20px;
                }
                
                h1 {
                    font-size: 2.5em;
                }
                
                .logo {
                    font-size: 5em;
                }
                
                .info {
                    grid-template-columns: 1fr;
                }
                
                .buttons {
                    flex-direction: column;
                }
                
                a {
                    width: 100%;
                    justify-content: center;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">🍽️</div>
            <h1>API Comanda</h1>
            <p class="subtitle">Sistema inteligente de gerenciamento de pedidos</p>
            
            <div class="info">
                <div class="info-box">
                    <strong>Versão</strong>
                    <span>v2.0</span>
                </div>
                <div class="info-box">
                    <strong>Status</strong>
                    <span><span class="status"></span>Online</span>
                </div>
            </div>
            
            <div class="framework-box">
                <strong>Framework</strong>
                <span>FastAPI</span>
            </div>
            
            <div class="buttons">
                <a href="/docs">
                    📚 Documentação Swagger
                </a>
                <a href="/redoc">
                    📖 ReDoc
                </a>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content 
