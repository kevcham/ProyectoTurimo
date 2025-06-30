from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Opinion(Base):
    __tablename__ = "opinion"

    id_opinion = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    id_actividad = Column(Integer, ForeignKey("actividad.id_actividad"))
    comentario = Column(String(255))
    calificacion = Column(Float)
    fecha = Column(DateTime)

    usuario = relationship("Usuario")
    actividad = relationship("Actividad")
