from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Auditoria(Base):
    __tablename__ = "auditoria"

    id_auditoria = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id_usuario"))
    usuario_nombre = Column(String(100))
    ip_origen = Column(String(50))
    tabla_afectada = Column(String(50))
    operacion = Column(String(50))
    descripcion = Column(String(255))
    fecha = Column(DateTime)

    usuario = relationship("Usuario")
