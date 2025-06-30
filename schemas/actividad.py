from pydantic import BaseModel
from datetime import datetime

class ActividadBase(BaseModel):
    id_tipo: int
    id_destino: int
    nombre: str
    descripcion: str | None = None
    precio: float | None = None
    duracion_horas: float | None = None
    fecha_inicio: datetime | None = None
    fecha_fin: datetime | None = None

class ActividadCreate(ActividadBase):
    pass

class ActividadOut(ActividadBase):
    id_actividad: int

    class Config:
        from_attributes = True
