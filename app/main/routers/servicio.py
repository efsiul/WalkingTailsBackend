from fastapi                            import APIRouter, HTTPException, Depends
from typing                             import List, Annotated
from sqlalchemy.orm                     import Session
from app.main.schemas.servicio          import ServicioBase, ServicioModel
from app.main.dependencies.db_session   import get_db
import app.main.models.servicio         as models

router        = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/servicio/", response_model=ServicioModel)
async def create_servicio(servicio: ServicioBase, db: db_dependency):
    db_servicio = models.Servicio(**servicio.model_dump())
    try:
        db.add(db_servicio)
        db.commit()
        db.refresh(db_servicio)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return db_servicio

@router.get("/servicio/", response_model=List[ServicioModel])
async def read_servicio(db: db_dependency):
    db_servicio = db.query(models.Servicio).all()
    return db_servicio

@router.get("/servicio/{servicio_id}", response_model=ServicioModel)
async def read_servicio(servicio_id: str, db: db_dependency):
    db_servicio = db.query(models.Servicio).filter(models.Servicio.id == servicio_id).first()
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio

@router.put("/servicio/{servicio_id}", response_model=ServicioModel)
async def update_servicio(servicio_id: str, servicio: ServicioBase, db: db_dependency):
    db_servicio = db.query(models.Servicio).filter(models.Servicio.id == servicio_id).first()
    if db_servicio is None:
        raise HTTPException(status_code=404, detail=" Servicio no encontrado")
    for var, value in vars(servicio).items():
        setattr(db_servicio, var, value) if value is not None else None
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

@router.delete("/servicio/{servicio_id}", status_code=204)
async def delete_servicio(servicio_id: str, db: db_dependency):
    db_servicio = db.query(models.Servicio).filter(models.Servicio.id == servicio_id).first()
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no existe")
    try:
        db.delete(db_servicio)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return {"detail": "Servicio ha sido eliminado"}

# Don't forget to handle exceptions and validate data as needed.