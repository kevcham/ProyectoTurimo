from sqlalchemy import Column, Integer, String, Float
from database import Base

class Destino(Base):
    __tablename__ = "destinos"

    id_destino = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    ubicacion = Column(String(255))
    icono = Column(String(255))
    latitud = Column(Float)
    longitud = Column(Float)
