from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.cita import ReservaMedica
from app.models.horario import HorarioDisponibilidad
from app.schemas.cita import CitaCreate

def agendar_cita(db: Session, cita: CitaCreate, paciente_id: int):
    # Reto avanzado: Verificar que exista y esté disponible[cite: 1]
    horario = db.query(HorarioDisponibilidad).filter(HorarioDisponibilidad.id == cita.horario_id).first()
    
    if not horario or not horario.esta_disponible:
        raise HTTPException(status_code=400, detail="El horario no existe o ya está ocupado")
    
    nueva_cita = ReservaMedica(paciente_id=paciente_id, horario_id=cita.horario_id)
    # Marcar horario como ocupado[cite: 1]
    horario.esta_disponible = False 
    
    db.add(nueva_cita)
    db.commit()
    db.refresh(nueva_cita)
    return nueva_cita

def listar_mis_citas(db: Session, paciente_id: int):
    # El paciente solo ve SUS citas filtrando con el ID del token[cite: 1]
    return db.query(ReservaMedica).filter(ReservaMedica.paciente_id == paciente_id).all()