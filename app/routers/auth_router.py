from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, Token
from app.services import usuario_service
from app.models.usuario import Usuario
from app.auth.seguridad import verificar_password, crear_token_acceso

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/registro", response_model=UsuarioResponse)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_service.crear_usuario(db, usuario)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Buscar al usuario por email (que en el form viene como username)[cite: 2]
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()
    
    # Mensaje genérico para no revelar si falló el correo o la clave[cite: 2]
    if not usuario or not verificar_password(form_data.password, usuario.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Crear token guardando el ID del usuario en el 'sub'[cite: 2]
    access_token = crear_token_acceso(data={"sub": str(usuario.id)})
    return {"access_token": access_token, "token_type": "bearer"}