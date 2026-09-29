from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class HorarioDisponibilidad(Base):
    __tablename__ = "horarios_disponibilidad"

    id = Column(Integer, primary_key=True, index=True)
    medico_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha_hora_inicio = Column(DateTime, nullable=False)
    fecha_hora_fin = Column(DateTime, nullable=False)
    esta_disponible = Column(Boolean, default=True) # Clave para el reto opcional

    medico = relationship("Usuario", back_populates="horarios")
    reserva = relationship("ReservaMedica", back_populates="horario", uselist=False)