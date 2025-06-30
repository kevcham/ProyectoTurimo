from pydantic import BaseModel

class DestinoBase(BaseModel):
    nombre: str
    descripcion: str | None = None
    ubicacion: str | None = None
    icono: str | None = None
    latitud: float | None = None
    longitud: float | None = None

class DestinoCreate(DestinoBase):
    pass

class DestinoOut(DestinoBase):
    id_destino: int

    class Config:
        from_attributes = True
