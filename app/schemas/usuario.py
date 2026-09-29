from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Schema de ENTRADA (Recibe la contraseña en texto plano)
class UsuarioCreate(BaseModel):
    nombre_completo: str
    email: EmailStr
    password: str

# Schema de SALIDA (Nunca incluye la contraseña)
class UsuarioResponse(BaseModel):
    id: int
    nombre_completo: str
    email: EmailStr
    rol: str
    fecha_registro: datetime

    class Config:
        from_attributes = True

# Schema para los Tokens
class Token(BaseModel):
    access_token: str
    token_type: str