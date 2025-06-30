from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.destino import Destino
from schemas.destino import DestinoCreate, DestinoOut

router = APIRouter(
    prefix="/destinos",
    tags=["Destinos"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[DestinoOut])
def listar_destinos(db: Session = Depends(get_db)):
    destinos = db.query(Destino).all()
    return destinos

@router.post("/", response_model=DestinoOut)
def crear_destino(destino: DestinoCreate, db: Session = Depends(get_db)):
    nuevo_destino = Destino(**destino.dict())
    db.add(nuevo_destino)
    db.commit()
    db.refresh(nuevo_destino)
    return nuevo_destino

@router.get("/{id_destino}", response_model=DestinoOut)
def obtener_destino(id_destino: int, db: Session = Depends(get_db)):
    destino = db.query(Destino).filter(Destino.id_destino == id_destino).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    return destino

@router.put("/{id_destino}", response_model=DestinoOut)
def actualizar_destino(id_destino: int, destino_data: DestinoCreate, db: Session = Depends(get_db)):
    destino = db.query(Destino).filter(Destino.id_destino == id_destino).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    for key, value in destino_data.dict().items():
        setattr(destino, key, value)
    db.commit()
    db.refresh(destino)
    return destino

@router.delete("/{id_destino}")
def eliminar_destino(id_destino: int, db: Session = Depends(get_db)):
    destino = db.query(Destino).filter(Destino.id_destino == id_destino).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    db.delete(destino)
    db.commit()
    return {"msg": "Destino eliminado correctamente"}
