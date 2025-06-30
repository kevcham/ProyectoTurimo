from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.actividad import Actividad
from schemas.actividad import ActividadCreate, ActividadOut

router = APIRouter(
    prefix="/actividades",
    tags=["Actividades"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ActividadOut])
def listar_actividades(db: Session = Depends(get_db)):
    actividades = db.query(Actividad).all()
    return actividades

@router.post("/", response_model=ActividadOut)
def crear_actividad(data: ActividadCreate, db: Session = Depends(get_db)):
    nueva = Actividad(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/{id_actividad}", response_model=ActividadOut)
def obtener_actividad(id_actividad: int, db: Session = Depends(get_db)):
    act = db.query(Actividad).filter(Actividad.id_actividad == id_actividad).first()
    if not act:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    return act

@router.put("/{id_actividad}", response_model=ActividadOut)
def actualizar_actividad(id_actividad: int, data: ActividadCreate, db: Session = Depends(get_db)):
    act = db.query(Actividad).filter(Actividad.id_actividad == id_actividad).first()
    if not act:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    
    for key, value in data.dict().items():
        setattr(act, key, value)
    
    db.commit()
    db.refresh(act)
    return act

@router.delete("/{id_actividad}")
def eliminar_actividad(id_actividad: int, db: Session = Depends(get_db)):
    act = db.query(Actividad).filter(Actividad.id_actividad == id_actividad).first()
    if not act:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    db.delete(act)
    db.commit()
    return {"msg": "Actividad eliminada correctamente"}
