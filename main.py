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

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Instancia FastAPI
app = FastAPI(
    title="API Turismo",
    description="Backend para gestión de turismo, actividades y reservas.",
    version="1.0.0"
)

# Configuración CORS
# Para desarrollo: dejar "*" para no tener bloqueos.
# Para producción: poner solo los dominios permitidos.
origins = [
    "http://localhost:3000",  
    "https://web-production-088e8.up.railway.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # ← Dejar "*" temporalmente para pruebas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta básica para comprobar funcionamiento
@app.get("/")
def read_root():
    return {"message": "API running on Railway!"}

# Incluir todos los routers
app.include_router(actividad.router, prefix="/actividad")
app.include_router(auditoria.router, prefix="/auditoria")
app.include_router(destinos.router, prefix="/destinos")
app.include_router(opinion.router, prefix="/opinion")
app.include_router(pais.router, prefix="/pais")
app.include_router(reserva.router, prefix="/reserva")
app.include_router(tipo_actividad.router, prefix="/tipo_actividad")
app.include_router(usuarios.router, prefix="/usuarios")

# Levantar servidor si se ejecuta localmente
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
