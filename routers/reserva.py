from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.reserva import Reserva
from schemas.reserva import ReservaCreate, ReservaOut

router = APIRouter(
    prefix="/reservas",
    tags=["Reservas"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ReservaOut])
def listar_reservas(db: Session = Depends(get_db)):
    reservas = db.query(Reserva).all()
    return reservas

@router.post("/", response_model=ReservaOut)
def crear_reserva(data: ReservaCreate, db: Session = Depends(get_db)):
    nueva = Reserva(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/{id_reserva}", response_model=ReservaOut)
def obtener_reserva(id_reserva: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id_reserva == id_reserva).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return reserva

@router.put("/{id_reserva}", response_model=ReservaOut)
def actualizar_reserva(id_reserva: int, data: ReservaCreate, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id_reserva == id_reserva).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")

    for key, value in data.dict().items():
        setattr(reserva, key, value)

    db.commit()
    db.refresh(reserva)
    return reserva

@router.delete("/{id_reserva}")
def eliminar_reserva(id_reserva: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id_reserva == id_reserva).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    db.delete(reserva)
    db.commit()
    return {"msg": "Reserva eliminada correctamente"}
