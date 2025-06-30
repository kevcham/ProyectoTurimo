from pydantic import BaseModel
from datetime import datetime

class AuditoriaBase(BaseModel):
    usuario_id: int
    usuario_nombre: str
    ip_origen: str
    tabla_afectada: str
    operacion: str
    descripcion: str
    fecha: datetime

class AuditoriaCreate(AuditoriaBase):
    pass

class AuditoriaOut(AuditoriaBase):
    id_auditoria: int

    class Config:
        from_attributes = True
