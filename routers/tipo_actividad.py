from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.tipo_actividad import TipoActividad
from schemas.tipo_actividad import TipoActividadCreate, TipoActividadOut

router = APIRouter(
    prefix="/tipo_actividad",
    tags=["TipoActividad"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[TipoActividadOut])
def listar_tipos(db: Session = Depends(get_db)):
    tipos = db.query(TipoActividad).all()
    return tipos

@router.post("/", response_model=TipoActividadOut)
def crear_tipo(tipo_data: TipoActividadCreate, db: Session = Depends(get_db)):
    nuevo_tipo = TipoActividad(**tipo_data.dict())
    db.add(nuevo_tipo)
    db.commit()
    db.refresh(nuevo_tipo)
    return nuevo_tipo

@router.get("/{id_tipo}", response_model=TipoActividadOut)
def obtener_tipo(id_tipo: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoActividad).filter(TipoActividad.id_tipo == id_tipo).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de actividad no encontrado")
    return tipo

@router.put("/{id_tipo}", response_model=TipoActividadOut)
def actualizar_tipo(id_tipo: int, tipo_data: TipoActividadCreate, db: Session = Depends(get_db)):
    tipo = db.query(TipoActividad).filter(TipoActividad.id_tipo == id_tipo).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de actividad no encontrado")
    tipo.tipo_actividad = tipo_data.tipo_actividad
    db.commit()
    db.refresh(tipo)
    return tipo

@router.delete("/{id_tipo}")
def eliminar_tipo(id_tipo: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoActividad).filter(TipoActividad.id_tipo == id_tipo).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de actividad no encontrado")
    db.delete(tipo)
    db.commit()
    return {"msg": "Tipo de actividad eliminado correctamente"}
