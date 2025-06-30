from pydantic import BaseModel

class TipoActividadBase(BaseModel):
    tipo_actividad: str

class TipoActividadCreate(TipoActividadBase):
    pass

class TipoActividadOut(TipoActividadBase):
    id_tipo: int

    class Config:
        from_attributes = True
