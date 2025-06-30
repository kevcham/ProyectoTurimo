from pydantic import BaseModel
from datetime import datetime

class ReservaBase(BaseModel):
    id_usuario: int
    id_actividad: int
    fecha_reserva: datetime
    estado: str
    num_personas: int
    total: float

class ReservaCreate(ReservaBase):
    pass

class ReservaOut(ReservaBase):
    id_reserva: int

    class Config:
        from_attributes = True
