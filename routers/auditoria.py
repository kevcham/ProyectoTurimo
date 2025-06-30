from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.auditoria import Auditoria
from schemas.auditoria import AuditoriaCreate, AuditoriaOut

router = APIRouter(
    prefix="/auditoria",
    tags=["Auditoría"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[AuditoriaOut])
def listar_logs(db: Session = Depends(get_db)):
    logs = db.query(Auditoria).order_by(Auditoria.fecha.desc()).all()
    return logs

@router.post("/", response_model=AuditoriaOut)
def registrar_log(log: AuditoriaCreate, db: Session = Depends(get_db)):
    nuevo_log = Auditoria(**log.dict())
    db.add(nuevo_log)
    db.commit()
    db.refresh(nuevo_log)
    return nuevo_log
