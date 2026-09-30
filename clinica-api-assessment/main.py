from fastapi import FastAPI
from database.connection import conn
from routes.users import user_router
from routes.patients import patient_router
from routes.appointments import appointment_router

app = FastAPI(title="API de Agendamento Clínico - Starter Kit")

# Registrando as rotas
app.include_router(user_router, prefix="/user")
app.include_router(patient_router, prefix="/patient")
app.include_router(appointment_router, prefix="/appointment")

@app.on_event("startup")
def on_startup():
    conn()

@app.get("/")
async def home():
    return {"message": "Bem-vindo à API da Clínica!"}