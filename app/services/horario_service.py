from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.horario import HorarioDisponibilidad
from app.schemas.horario import HorarioCreate

def crear_horario(db: Session, horario: HorarioCreate, medico_id: int):
    # El ID del médico sale del token automáticamente[cite: 1]
    nuevo_horario = HorarioDisponibilidad(**horario.dict(), medico_id=medico_id)
    db.add(nuevo_horario)
    db.commit()
    db.refresh(nuevo_horario)
    return nuevo_horario

def eliminar_horario(db: Session, horario_id: int, medico_id: int):
    horario = db.query(HorarioDisponibilidad).filter(HorarioDisponibilidad.id == horario_id).first()
    if not horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    
    # Autorización a nivel de dato: Un médico NO puede borrar la agenda de otro[cite: 1]
    if horario.medico_id != medico_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No puedes modificar un horario ajeno")
    
    db.delete(horario)
    db.commit()
    return {"mensaje": "Horario eliminado correctamente"}