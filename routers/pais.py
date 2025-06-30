from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.pais import Pais
from schemas.pais import PaisCreate, PaisOut

router = APIRouter(
    prefix="/pais",
    tags=["Pais"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[PaisOut])
def listar_paises(db: Session = Depends(get_db)):
    paises = db.query(Pais).all()
    return paises

@router.post("/", response_model=PaisOut)
def crear_pais(pais_data: PaisCreate, db: Session = Depends(get_db)):
    nuevo_pais = Pais(**pais_data.dict())
    db.add(nuevo_pais)
    db.commit()
    db.refresh(nuevo_pais)
    return nuevo_pais

@router.get("/{id_pais}", response_model=PaisOut)
def obtener_pais(id_pais: int, db: Session = Depends(get_db)):
    pais = db.query(Pais).filter(Pais.id_pais == id_pais).first()
    if not pais:
        raise HTTPException(status_code=404, detail="País no encontrado")
    return pais

@router.put("/{id_pais}", response_model=PaisOut)
def actualizar_pais(id_pais: int, pais_data: PaisCreate, db: Session = Depends(get_db)):
    pais = db.query(Pais).filter(Pais.id_pais == id_pais).first()
    if not pais:
        raise HTTPException(status_code=404, detail="País no encontrado")
    pais.pais = pais_data.pais
    db.commit()
    db.refresh(pais)
    return pais

@router.delete("/{id_pais}")
def eliminar_pais(id_pais: int, db: Session = Depends(get_db)):
    pais = db.query(Pais).filter(Pais.id_pais == id_pais).first()
    if not pais:
        raise HTTPException(status_code=404, detail="País no encontrado")
    db.delete(pais)
    db.commit()
    return {"msg": "País eliminado correctamente"}
