from pydantic import BaseModel
from typing import Optional
import datetime

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: Optional[datetime.date]
    email: str
    rol: Optional[str] = "usuario"

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    fecha_nacimiento: Optional[datetime.date]
    email: Optional[str]
    contrasena: Optional[str]

class UsuarioOut(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True
