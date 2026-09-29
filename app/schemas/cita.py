from pydantic import BaseModel
from datetime import datetime

class CitaCreate(BaseModel):
    horario_id: int

class CitaResponse(BaseModel):
    id: int
    paciente_id: int
    horario_id: int
    estado: str
    fecha_creacion: datetime

    class Config:
        from_attributes = True