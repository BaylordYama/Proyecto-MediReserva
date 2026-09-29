from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.auth.dependencias import obtener_usuario_actual
from app.models.usuario import Usuario
from app.schemas.cita import CitaCreate, CitaResponse
from app.services import cita_service

router = APIRouter(prefix="/citas", tags=["Citas (Pacientes)"])

@router.post("/", response_model=CitaResponse)
def agendar_cita(cita: CitaCreate, db: Session = Depends(get_db), paciente: Usuario = Depends(obtener_usuario_actual)):
    return cita_service.agendar_cita(db, cita, paciente.id)

@router.get("/mis-citas", response_model=List[CitaResponse])
def mis_citas(db: Session = Depends(get_db), paciente: Usuario = Depends(obtener_usuario_actual)):
    return cita_service.listar_mis_citas(db, paciente.id)