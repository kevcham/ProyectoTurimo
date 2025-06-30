from pydantic import BaseModel
from datetime import datetime

class OpinionBase(BaseModel):
    id_usuario: int
    id_actividad: int
    comentario: str
    calificacion: float
    fecha: datetime

class OpinionCreate(OpinionBase):
    pass

class OpinionOut(OpinionBase):
    id_opinion: int

    class Config:
     from_attributes = True
