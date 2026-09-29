from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    rol = Column(String, default="paciente", nullable=False) # Roles: paciente, medico, admin
    especialidad = Column(String, nullable=True) # Solo se llena si es médico
    fecha_registro = Column(DateTime, default=datetime.utcnow)

    # Relaciones para navegar a través de los datos
    horarios = relationship("HorarioDisponibilidad", back_populates="medico")
    citas_como_paciente = relationship("ReservaMedica", foreign_keys="[ReservaMedica.paciente_id]", back_populates="paciente")