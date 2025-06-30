from sqlalchemy import Column, Integer, DateTime, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Reserva(Base):
    __tablename__ = "reserva"

    id_reserva = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    id_actividad = Column(Integer, ForeignKey("actividad.id_actividad"))
    fecha_reserva = Column(DateTime)
    estado = Column(String(50))
    num_personas = Column(Integer)
    total = Column(Float)

    usuario = relationship("Usuario")
    actividad = relationship("Actividad")
