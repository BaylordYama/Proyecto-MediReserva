from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class ReservaMedica(Base):
    __tablename__ = "reservas_medicas"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    horario_id = Column(Integer, ForeignKey("horarios_disponibilidad.id"), nullable=False, unique=True)
    estado = Column(String, default="confirmada") # confirmada, cancelada, completada
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    paciente = relationship("Usuario", foreign_keys=[paciente_id], back_populates="citas_como_paciente")
    horario = relationship("HorarioDisponibilidad", back_populates="reserva")