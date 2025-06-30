from pydantic import BaseModel

class PaisBase(BaseModel):
    pais: str

class PaisCreate(PaisBase):
    pass

class PaisOut(PaisBase):
    id_pais: int

    class Config:
        from_attributes = True
