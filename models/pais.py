from sqlalchemy import Column, Integer, String
from database import Base

class Pais(Base):
    __tablename__ = "pais"

    id_pais = Column(Integer, primary_key=True, autoincrement=True)
    pais = Column(String(100), nullable=False)
