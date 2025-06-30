from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import enum

class RolEnum(enum.Enum):
    usuario = "usuario"
    admin = "admin"

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, index=True)
    id_pais = Column(Integer, ForeignKey("pais.id_pais"))
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date)
    email = Column(String(150), unique=True, nullable=False)
    contrasena = Column(String(255))
    rol = Column(Enum(RolEnum), default="usuario")
    google_id = Column(String(50))
    api_key = Column(String(50))

    pais = relationship("Pais")
