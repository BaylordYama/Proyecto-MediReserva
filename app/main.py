from fastapi import FastAPI
from app.database import engine, Base
from app.models.usuario import Usuario
from app.models.horario import HorarioDisponibilidad
from app.models.cita import ReservaMedica
from app.routers import auth_router, horario_router, cita_router

# Crea las tablas en PostgreSQL si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MediReserva API",
    description="Sistema backend seguro para reservas médicas.",
    version="1.0.0"
)


app.include_router(auth_router.router)
app.include_router(horario_router.router)
app.include_router(cita_router.router)

@app.get("/")
def estado_servidor():
    return {"mensaje": "API de MediReserva funcionando correctamente. Ve a /docs para probar."}