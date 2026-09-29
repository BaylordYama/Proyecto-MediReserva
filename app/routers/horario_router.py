from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.auth.dependencias import exigir_rol_medico
from app.models.usuario import Usuario
from app.schemas.horario import HorarioCreate, HorarioResponse
from app.services import horario_service

router = APIRouter(prefix="/horarios", tags=["Horarios (Médicos)"])

@router.post("/", response_model=HorarioResponse)
def crear_horario(horario: HorarioCreate, db: Session = Depends(get_db), medico: Usuario = Depends(exigir_rol_medico)):
    return horario_service.crear_horario(db, horario, medico.id)

@router.delete("/{horario_id}")
def eliminar_horario(horario_id: int, db: Session = Depends(get_db), medico: Usuario = Depends(exigir_rol_medico)):
    return horario_service.eliminar_horario(db, horario_id, medico.id)