from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    excepcion_credenciales = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"}, # Estándar para error 401[cite: 1]
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        usuario_id: str = payload.get("sub")
        if usuario_id is None:
            raise excepcion_credenciales
    except JWTError:
        raise excepcion_credenciales
        
    usuario = db.query(Usuario).filter(Usuario.id == int(usuario_id)).first()
    if usuario is None:
        raise excepcion_credenciales
    return usuario

def exigir_rol_medico(usuario_actual: Usuario = Depends(obtener_usuario_actual)):
    if usuario_actual.rol != "medico":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, # 403: Sé quién eres pero no te corresponde[cite: 1]
            detail="Se requiere rol de médico."
        )
    return usuario_actual

def exigir_rol_admin(usuario_actual: Usuario = Depends(obtener_usuario_actual)):
    if usuario_actual.rol != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Se requiere rol de administrador."
        )
    return usuario_actual