from sqlalchemy import Column, Integer, String
from database import Base

class TipoActividad(Base):
    __tablename__ = "tipo_actividad"

    id_tipo = Column(Integer, primary_key=True, autoincrement=True)
    tipo_actividad = Column(String(100), nullable=False)
