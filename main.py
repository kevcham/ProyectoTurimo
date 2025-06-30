import os
import uvicorn
from fastapi import FastAPI
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

# Crea las tablas en la DB (si no existen)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Turismo",
    description="Backend para gestión de turismo, actividades y reservas.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "API running on Railway!"}

# Incluir tus routers
app.include_router(actividad.router)
app.include_router(auditoria.router)
app.include_router(destinos.router)
app.include_router(opinion.router)
app.include_router(pais.router)
app.include_router(reserva.router)
app.include_router(tipo_actividad.router)
app.include_router(usuarios.router)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
