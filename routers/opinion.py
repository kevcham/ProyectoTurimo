from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.opinion import OpinionCreate, OpinionOut
from models.opinion import Opinion


router = APIRouter(
    prefix="/opiniones",
    tags=["Opiniones"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[OpinionOut])
def listar_opiniones(db: Session = Depends(get_db)):
    opiniones = db.query(Opinion).all()
    return opiniones

@router.post("/", response_model=OpinionOut)
def crear_opinion(opinion: OpinionCreate, db: Session = Depends(get_db)):
    nueva = Opinion(**opinion.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/{id_opinion}", response_model=OpinionOut)
def obtener_opinion(id_opinion: int, db: Session = Depends(get_db)):
    op = db.query(Opinion).filter(Opinion.id_opinion == id_opinion).first()
    if not op:
        raise HTTPException(status_code=404, detail="Opinión no encontrada")
    return op

@router.put("/{id_opinion}", response_model=OpinionOut)
def actualizar_opinion(id_opinion: int, opinion_data: OpinionCreate, db: Session = Depends(get_db)):
    op = db.query(Opinion).filter(Opinion.id_opinion == id_opinion).first()
    if not op:
        raise HTTPException(status_code=404, detail="Opinión no encontrada")
    
    for key, value in opinion_data.dict().items():
        setattr(op, key, value)

    db.commit()
    db.refresh(op)
    return op

@router.delete("/{id_opinion}")
def eliminar_opinion(id_opinion: int, db: Session = Depends(get_db)):
    op = db.query(Opinion).filter(Opinion.id_opinion == id_opinion).first()
    if not op:
        raise HTTPException(status_code=404, detail="Opinión no encontrada")
    db.delete(op)
    db.commit()
    return {"msg": "Opinión eliminada correctamente"}
