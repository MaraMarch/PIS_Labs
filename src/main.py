from fastapi import FastAPI
from fastapi.responses import HTMLResponse # Добавь этот импорт!
from src.api.v1.endpoints import router as api_router
from src.infrastructure.db.database import engine, Base
import src.infrastructure.db.models

app = FastAPI(title="Incident System")

# Подключаем роуты API
app.include_router(api_router, prefix="/api/v1")

# --- ВОТ ЭТОТ БЛОК СОЗДАСТ КРАСИВУЮ ШАПКУ ---
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Incident Control Center</title>
            <style>
                body {
                    font-family: 'Segoe UI', sans-serif;
                    background-color: #0f172a;
                    color: #f8fafc;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }
                .card {
                    background: #1e293b;
                    padding: 40px;
                    border-radius: 20px;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.5);
                    text-align: center;
                    border: 1px solid #334155;
                }
                h1 { color: #38bdf8; margin-bottom: 10px; }
                p { color: #94a3b8; margin-bottom: 30px; }
                .btn {
                    background: linear-gradient(135deg, #38bdf8 0%, #2563eb 100%);
                    color: white;
                    padding: 15px 35px;
                    text-decoration: none;
                    border-radius: 12px;
                    font-weight: bold;
                    transition: transform 0.2s, box-shadow 0.2s;
                    display: inline-block;
                }
                .btn:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 5px 15px rgba(56, 189, 248, 0.4);
                }
                .status {
                    margin-top: 20px;
                    font-size: 0.9rem;
                    color: #4ade80;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🚀 Incident System v0.1</h1>
                <p>Микросервисная архитектура: FastAPI + gRPC + SQLAlchemy</p>
                <a href="/docs" class="btn">ОТКРЫТЬ ДОКУМЕНТАЦИЮ (Swagger)</a>
                <div class="status">● Система работает в штатном режиме</div>
            </div>
        </body>
    </html>
    """
# ---------------------------------------------

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
