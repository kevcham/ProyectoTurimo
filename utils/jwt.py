import jwt
from datetime import datetime, timedelta

# Clave secreta (puedes cambiarla por una más segura y guardarla en un .env)
SECRET_KEY = "tu_clave_secreta_123"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60  # 1 hora

# Crear un token JWT con datos del usuario
def crear_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Verificar un token JWT (opcional para endpoints protegidos)
def verificar_token(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expirado")
    except jwt.InvalidTokenError:
        raise ValueError("Token inválido")
