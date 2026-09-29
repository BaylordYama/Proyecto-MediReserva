from pydantic import BaseModel
from datetime import datetime

class HorarioCreate(BaseModel):
    fecha_hora_inicio: datetime
    fecha_hora_fin: datetime

class HorarioResponse(BaseModel):
    id: int
    medico_id: int
    fecha_hora_inicio: datetime
    fecha_hora_fin: datetime
    esta_disponible: bool

    class Config:
        from_attributes = True