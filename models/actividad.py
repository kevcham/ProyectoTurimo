from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Actividad(Base):
    __tablename__ = "actividad"

    id_actividad = Column(Integer, primary_key=True, autoincrement=True)
    id_tipo = Column(Integer, ForeignKey("tipo_actividad.id_tipo"))
    id_destino = Column(Integer, ForeignKey("destinos.id_destino"))
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    precio = Column(Float)
    duracion_horas = Column(Float)
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)

    tipo = relationship("TipoActividad")
    destino = relationship("Destino")
