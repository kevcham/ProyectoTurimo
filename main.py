import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import (
    actividad,
    auditoria,
    destinos,
    opinion,
    pais,
    reserva,
    tipo_actividad,
    usuarios
)

# -------------------------------
# Crear las tablas en la BD (si no existen)
# -------------------------------
Base.metadata.create_all(bind=engine)

# -------------------------------
# Crear la app FastAPI
# -------------------------------
app = FastAPI(
    title="API Turismo",
    description="Backend para gestión de turismo, actividades y reservas.",
    version="1.0.0"
)

# -------------------------------
# Configuración de CORS
# -------------------------------
origins = [
    "http://localhost:3000",  
    "https://mi-frontend.com",  
    "https://web-production-088e8.up.railway.app"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # puedes usar ["*"] si quieres permitir todos los dominios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Rutas de prueba
# -------------------------------
@app.get("/")
def read_root():
    return {"message": "API running on Railway!"}

# -------------------------------
# Incluir todos los routers
# -------------------------------
app.include_router(actividad.router)
app.include_router(auditoria.router)
app.include_router(destinos.router)
app.include_router(opinion.router)
app.include_router(pais.router)
app.include_router(reserva.router)
app.include_router(tipo_actividad.router)
app.include_router(usuarios.router)

# -------------------------------
# Configuración para Railway
# -------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
