from fastapi.responses import HTMLResponse
from src.app import app

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
        <title>API Comanda — Gestão de Pedidos</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">
        <style>
            :root {
                --gold: #c9a84c;
                --gold-light: #e8c97a;
                --gold-dim: rgba(201, 168, 76, 0.15);
                --cream: #f5efe6;
                --ink: #0c0a07;
                --ink-mid: #1a1710;
                --ink-soft: #2d2820;
                --smoke: rgba(245, 239, 230, 0.06);
                --smoke-mid: rgba(245, 239, 230, 0.12);
            }

            * { margin: 0; padding: 0; box-sizing: border-box; }

            html, body {
                height: 100%;
                font-family: 'DM Mono', monospace;
                background: var(--ink);
                color: var(--cream);
                overflow: hidden;
            }

            /* === CANVAS BACKGROUND === */
            canvas {
                position: fixed;
                inset: 0;
                z-index: 0;
                opacity: 0.35;
            }

            /* === NOISE OVERLAY === */
            body::after {
                content: '';
                position: fixed;
                inset: 0;
                background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='1'/%3E%3C/svg%3E");
                opacity: 0.04;
                z-index: 1;
                pointer-events: none;
            }

            /* === LAYOUT === */
            .stage {
                position: relative;
                z-index: 2;
                min-height: 100vh;
                display: grid;
                grid-template-columns: 1fr 420px 1fr;
                grid-template-rows: 1fr auto 1fr;
                align-items: center;
            }

            /* === LEFT COLUMN (decorative) === */
            .left-deco {
                grid-column: 1;
                grid-row: 1 / 4;
                display: flex;
                flex-direction: column;
                align-items: flex-end;
                padding-right: 60px;
                gap: 30px;
                opacity: 0;
                animation: fadeSlideRight 1s ease 0.8s forwards;
            }

            .deco-line {
                width: 1px;
                height: 120px;
                background: linear-gradient(to bottom, transparent, var(--gold), transparent);
            }

            .deco-text {
                font-size: 0.6rem;
                letter-spacing: 0.4em;
                color: var(--gold);
                text-transform: uppercase;
                writing-mode: vertical-rl;
                text-orientation: mixed;
                opacity: 0.6;
            }

            .deco-circle {
                width: 6px;
                height: 6px;
                border-radius: 50%;
                border: 1px solid var(--gold);
                opacity: 0.5;
            }

            /* === RIGHT COLUMN (decorative) === */
            .right-deco {
                grid-column: 3;
                grid-row: 1 / 4;
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                padding-left: 60px;
                gap: 20px;
                opacity: 0;
                animation: fadeSlideLeft 1s ease 0.8s forwards;
            }

            .right-deco .deco-label {
                font-size: 0.55rem;
                letter-spacing: 0.35em;
                color: rgba(245,239,230,0.3);
                text-transform: uppercase;
            }

            .right-deco .deco-val {
                font-size: 0.7rem;
                color: var(--gold);
                letter-spacing: 0.1em;
            }

            .right-deco .sep {
                width: 40px;
                height: 1px;
                background: var(--gold-dim);
                margin: 8px 0;
            }

            /* === CENTER CARD === */
            .card {
                grid-column: 2;
                grid-row: 2;
                padding: 60px 48px 52px;
                background: linear-gradient(160deg, var(--ink-soft) 0%, var(--ink-mid) 100%);
                border: 1px solid rgba(201, 168, 76, 0.2);
                border-radius: 4px;
                position: relative;
                opacity: 0;
                animation: riseIn 1s cubic-bezier(0.16, 1, 0.3, 1) 0.1s forwards;
            }

            /* Corner ornaments */
            .card::before, .card::after,
            .card .corner-br, .card .corner-bl {
                content: '';
                position: absolute;
                width: 18px;
                height: 18px;
            }
            .card::before {
                top: -1px; left: -1px;
                border-top: 2px solid var(--gold);
                border-left: 2px solid var(--gold);
            }
            .card::after {
                top: -1px; right: -1px;
                border-top: 2px solid var(--gold);
                border-right: 2px solid var(--gold);
            }
            .card .corner-br {
                bottom: -1px; right: -1px;
                border-bottom: 2px solid var(--gold);
                border-right: 2px solid var(--gold);
            }
            .card .corner-bl {
                bottom: -1px; left: -1px;
                border-bottom: 2px solid var(--gold);
                border-left: 2px solid var(--gold);
            }

            /* === HEADER === */
            .eyebrow {
                font-size: 0.55rem;
                letter-spacing: 0.5em;
                color: var(--gold);
                text-transform: uppercase;
                margin-bottom: 28px;
                display: flex;
                align-items: center;
                gap: 14px;
            }
            .eyebrow::before, .eyebrow::after {
                content: '';
                flex: 1;
                height: 1px;
                background: linear-gradient(to right, transparent, rgba(201, 168, 76, 0.4));
            }
            .eyebrow::after {
                background: linear-gradient(to left, transparent, rgba(201, 168, 76, 0.4));
            }

            .icon-wrap {
                display: flex;
                justify-content: center;
                margin-bottom: 20px;
            }

            .icon-ring {
                width: 72px;
                height: 72px;
                border-radius: 50%;
                border: 1px solid rgba(201, 168, 76, 0.3);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2rem;
                position: relative;
                animation: spinRing 20s linear infinite;
            }

            .icon-ring::before {
                content: '';
                position: absolute;
                inset: 4px;
                border-radius: 50%;
                border: 1px solid rgba(201, 168, 76, 0.15);
            }

            @keyframes spinRing {
                from { box-shadow: 0 0 0 0 rgba(201,168,76,0.2), inset 0 0 20px rgba(201,168,76,0.05); }
                50% { box-shadow: 0 0 30px rgba(201,168,76,0.15), inset 0 0 20px rgba(201,168,76,0.1); }
                to { box-shadow: 0 0 0 0 rgba(201,168,76,0.2), inset 0 0 20px rgba(201,168,76,0.05); }
            }

            h1 {
                font-family: 'Cormorant Garamond', serif;
                font-size: 3.6rem;
                font-weight: 300;
                letter-spacing: -0.01em;
                text-align: center;
                line-height: 1;
                margin-bottom: 10px;
                background: linear-gradient(135deg, var(--cream) 30%, var(--gold-light) 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }

            h1 em {
                font-style: italic;
                font-weight: 300;
            }

            .subtitle {
                text-align: center;
                font-size: 0.62rem;
                letter-spacing: 0.25em;
                color: rgba(245, 239, 230, 0.4);
                text-transform: uppercase;
                margin-bottom: 44px;
            }

            /* === DIVIDER === */
            .divider {
                display: flex;
                align-items: center;
                gap: 12px;
                margin: 32px 0;
            }
            .divider::before, .divider::after {
                content: '';
                flex: 1;
                height: 1px;
                background: linear-gradient(to right, transparent, rgba(245,239,230,0.08));
            }
            .divider::after {
                background: linear-gradient(to left, transparent, rgba(245,239,230,0.08));
            }
            .divider-diamond {
                width: 5px;
                height: 5px;
                border: 1px solid rgba(201,168,76,0.5);
                transform: rotate(45deg);
            }

            /* === STATS GRID === */
            .stats {
                display: grid;
                grid-template-columns: 1fr 1px 1fr;
                gap: 0;
                margin-bottom: 40px;
            }

            .stat-sep {
                background: rgba(245,239,230,0.07);
            }

            .stat {
                padding: 22px 24px;
                text-align: center;
            }

            .stat-label {
                font-size: 0.52rem;
                letter-spacing: 0.4em;
                color: rgba(245,239,230,0.35);
                text-transform: uppercase;
                margin-bottom: 10px;
                display: block;
            }

            .stat-value {
                font-family: 'Cormorant Garamond', serif;
                font-size: 2rem;
                font-weight: 300;
                color: var(--cream);
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
            }

            .pulse-dot {
                width: 7px;
                height: 7px;
                border-radius: 50%;
                background: #4ade80;
                position: relative;
                flex-shrink: 0;
            }
            .pulse-dot::after {
                content: '';
                position: absolute;
                inset: -4px;
                border-radius: 50%;
                border: 1px solid #4ade80;
                animation: expandPulse 2s ease-out infinite;
            }
            @keyframes expandPulse {
                0% { opacity: 0.8; transform: scale(0.6); }
                100% { opacity: 0; transform: scale(2); }
            }

            /* === FRAMEWORK BADGE === */
            .framework-row {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 14px;
                padding: 14px 0;
                margin-bottom: 40px;
                border-top: 1px solid rgba(245,239,230,0.06);
                border-bottom: 1px solid rgba(245,239,230,0.06);
            }
            .framework-label {
                font-size: 0.52rem;
                letter-spacing: 0.4em;
                color: rgba(245,239,230,0.3);
                text-transform: uppercase;
            }
            .framework-value {
                font-size: 0.7rem;
                letter-spacing: 0.15em;
                color: var(--gold);
                font-weight: 500;
            }
            .framework-dot {
                width: 3px;
                height: 3px;
                border-radius: 50%;
                background: rgba(245,239,230,0.2);
            }

            /* === BUTTONS === */
            .actions {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 12px;
            }

            .btn {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                padding: 16px 20px;
                text-decoration: none;
                font-size: 0.58rem;
                letter-spacing: 0.3em;
                text-transform: uppercase;
                font-family: 'DM Mono', monospace;
                border-radius: 2px;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }

            .btn-primary {
                background: linear-gradient(135deg, var(--gold) 0%, #a8872e 100%);
                color: var(--ink);
                font-weight: 500;
            }

            .btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 32px rgba(201, 168, 76, 0.35);
                filter: brightness(1.1);
            }

            .btn-secondary {
                background: transparent;
                color: var(--cream);
                border: 1px solid rgba(245,239,230,0.15);
            }

            .btn-secondary:hover {
                border-color: var(--gold);
                color: var(--gold);
                transform: translateY(-2px);
                background: var(--gold-dim);
            }

            .btn-icon {
                font-size: 0.85rem;
            }

            /* === FOOTER === */
            .card-footer {
                margin-top: 28px;
                text-align: center;
                font-size: 0.5rem;
                letter-spacing: 0.3em;
                color: rgba(245,239,230,0.2);
                text-transform: uppercase;
            }

            /* === ANIMATIONS === */
            @keyframes riseIn {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes fadeSlideRight {
                from { opacity: 0; transform: translateX(-20px); }
                to { opacity: 1; transform: translateX(0); }
            }
            @keyframes fadeSlideLeft {
                from { opacity: 0; transform: translateX(20px); }
                to { opacity: 1; transform: translateX(0); }
            }

            /* === RESPONSIVE === */
            @media (max-width: 900px) {
                .stage {
                    grid-template-columns: 1fr;
                    grid-template-rows: auto;
                    padding: 40px 20px;
                    overflow-y: auto;
                    min-height: 100dvh;
                }
                .left-deco, .right-deco { display: none; }
                .card {
                    grid-column: 1;
                    grid-row: 1;
                    padding: 44px 28px 36px;
                }
                h1 { font-size: 2.8rem; }
                .actions { grid-template-columns: 1fr; }
            }
        </style>
    </head>
    <body>
        <canvas id="bg"></canvas>

        <div class="stage">

            <!-- LEFT DECORATION -->
            <div class="left-deco">
                <div class="deco-circle"></div>
                <div class="deco-text">Sistema de Comandas</div>
                <div class="deco-line"></div>
                <div class="deco-circle"></div>
            </div>

            <!-- MAIN CARD -->
            <div class="card">
                <div class="corner-br"></div>
                <div class="corner-bl"></div>

                <div class="eyebrow">Gestão de Pedidos</div>

                <div class="icon-wrap">
                    <div class="icon-ring">🍽️</div>
                </div>

                <h1>API <em>Comanda</em></h1>
                <p class="subtitle">Sistema inteligente de gerenciamento de pedidos</p>

                <div class="stats">
                    <div class="stat">
                        <span class="stat-label">Versão</span>
                        <span class="stat-value">v2.0</span>
                    </div>
                    <div class="stat-sep"></div>
                    <div class="stat">
                        <span class="stat-label">Status</span>
                        <span class="stat-value">
                            <span class="pulse-dot"></span>
                            Online
                        </span>
                    </div>
                </div>

                <div class="framework-row">
                    <span class="framework-label">Framework</span>
                    <span class="framework-dot"></span>
                    <span class="framework-value">FastAPI</span>
                    <span class="framework-dot"></span>
                    <span class="framework-label">Python</span>
                </div>

                <div class="actions">
                    <a href="/docs" class="btn btn-primary">
                        <span class="btn-icon">⚡</span>
                        Swagger UI
                    </a>
                    <a href="/redoc" class="btn btn-secondary">
                        <span class="btn-icon">📖</span>
                        ReDoc
                    </a>
                </div>

                <p class="card-footer">© 2025 API Comanda &nbsp;·&nbsp; All rights reserved</p>
            </div>

            <!-- RIGHT DECORATION -->
            <div class="right-deco">
                <span class="deco-label">Endpoints</span>
                <span class="deco-val">/docs</span>
                <div class="sep"></div>
                <span class="deco-label">Schema</span>
                <span class="deco-val">/redoc</span>
                <div class="sep"></div>
                <span class="deco-label">Health</span>
                <span class="deco-val">/health</span>
            </div>

        </div>

        <script>
        // Ambient particle canvas
        const canvas = document.getElementById('bg');
        const ctx = canvas.getContext('2d');

        let W, H, particles = [];
        const GOLD = [201, 168, 76];

        function resize() {
            W = canvas.width = window.innerWidth;
            H = canvas.height = window.innerHeight;
        }

        function createParticle() {
            return {
                x: Math.random() * W,
                y: Math.random() * H,
                r: Math.random() * 1.5 + 0.3,
                vx: (Math.random() - 0.5) * 0.3,
                vy: -Math.random() * 0.4 - 0.1,
                life: 0,
                maxLife: Math.random() * 300 + 150
            };
        }

        function init() {
            resize();
            particles = Array.from({ length: 80 }, createParticle);
        }

        function draw() {
            ctx.clearRect(0, 0, W, H);

            // Draw connection lines
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 120) {
                        const alpha = (1 - dist / 120) * 0.12;
                        ctx.strokeStyle = `rgba(${GOLD},${alpha})`;
                        ctx.lineWidth = 0.5;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }

            // Draw particles
            particles.forEach(p => {
                p.life++;
                p.x += p.vx;
                p.y += p.vy;

                const progress = p.life / p.maxLife;
                const alpha = progress < 0.2
                    ? progress / 0.2
                    : progress > 0.8
                    ? 1 - (progress - 0.8) / 0.2
                    : 1;

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(${GOLD},${alpha * 0.6})`;
                ctx.fill();

                if (p.life >= p.maxLife || p.y < -10) {
                    Object.assign(p, createParticle());
                    p.y = H + 10;
                }
            });

            requestAnimationFrame(draw);
        }

        window.addEventListener('resize', resize);
        init();
        draw();
        </script>
    </body>
    </html>
    """
    return html_content