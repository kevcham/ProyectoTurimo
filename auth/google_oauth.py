from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests

from database import SessionLocal
from models.usuario import Usuario
from schemas.google_login import GoogleToken
from utils.jwt import crear_token  # <-- IMPORTANTE

# Client ID de Google (reemplázalo si cambia)
CLIENT_ID = "790904165713-v2q7ndirtme872t72igl1dv46k3s6bvd.apps.googleusercontent.com"

# Crear router
router = APIRouter(prefix="/auth", tags=["Autenticación"])

# Función para obtener conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para verificar token de Google
def verificar_token_google(token_id: str):
    try:
        idinfo = id_token.verify_oauth2_token(
            token_id, requests.Request(), CLIENT_ID
        )
        return {
            "google_id": idinfo["sub"],
            "correo": idinfo["email"],
            "nombre": idinfo["name"]
        }
    except Exception:
        raise HTTPException(status_code=401, detail="Token de Google inválido")

# Ruta de login con Google
@router.post("/google-login")
def login_google(data: GoogleToken, db: Session = Depends(get_db)):
    datos_google = verificar_token_google(data.token_id)

    # Buscar si ya existe el usuario
    usuario = db.query(Usuario).filter(
        Usuario.google_id == datos_google["google_id"]
    ).first()

    # Si no existe, lo registra automáticamente
    if not usuario:
        usuario = Usuario(
            nombre=datos_google["nombre"],
            correo=datos_google["correo"],
            google_id=datos_google["google_id"],
            rol="usuario"
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)

    # Generar token JWT personalizado
    token_jwt = crear_token({
        "id": usuario.id,
        "correo": usuario.correo,
        "nombre": usuario.nombre,
        "rol": usuario.rol
    })

    return {
        "msg": "Login correcto",
        "token": token_jwt,
        "usuario": {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "correo": usuario.correo,
            "rol": usuario.rol
        }
    }
