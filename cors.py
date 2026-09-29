from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origens_permitidas = [
    "https://meu-frontend-confiavel.com",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origens_permitidas,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
)

@app.get("/")
async def read_root():
    return {"mensagem": "CORS configurado com sucesso no FastAPI!"}