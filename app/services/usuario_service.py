from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.auth.seguridad import obtener_hash_password

def crear_usuario(db: Session, usuario: UsuarioCreate):
    # Validar si el email ya existe
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    # Hashear la contraseña y forzar el rol por defecto (paciente)[cite: 2]
    nuevo_usuario = Usuario(
        nombre_completo=usuario.nombre_completo,
        email=usuario.email,
        password_hash=obtener_hash_password(usuario.password),
        rol="paciente" 
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario