from fastapi                            import APIRouter, HTTPException, Depends
from typing                             import List, Annotated
from sqlalchemy.orm                     import Session
from app.main.schemas.estilizado        import EstilizadoApi, EstilizadoModel
from app.main.dependencies.db_session   import get_db
import app.main.models.estilizado       as models

router          = APIRouter()
db_dependency   = Annotated[Session, Depends(get_db)]

@router.post("/estilizado/", response_model=EstilizadoApi)
async def create_estilizado(estilizado: EstilizadoApi, db: db_dependency):
    db_estilizado = models.Estilizado(**estilizado.model_dump())
    try:
        db.add(db_estilizado)
        db.commit()
        db.refresh(db_estilizado)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return db_estilizado.to_api()

@router.get("/estilizado/", response_model=List[EstilizadoApi])
async def read_estilizado(db: db_dependency):
    db_estilizados = db.query(models.Estilizado).all()
    return [e.dict() for e in db_estilizados]

@router.get("/estilizado/{estilizado_id}", response_model=EstilizadoModel)
async def read_estilizado(estilizado_id: int, db: db_dependency):
    db_estilizado = db.query(models.Estilizado).filter(models.Estilizado.id == estilizado_id).first()
    if db_estilizado is None:
        raise HTTPException(status_code=404, detail="Servicio de estilizado no encontrado")
    return db_estilizado.dict()

@router.put("/estilizado/{estilizado_id}", response_model=EstilizadoModel)
async def update_estilizado(estilizado_id: int, estilo: EstilizadoApi, db: db_dependency):
    db_estilizado = db.query(models.Estilizado).filter(models.Estilizado.id == estilizado_id).first()
    if db_estilizado is None:
        raise HTTPException(status_code=404, detail="Servicio de estilizado no encontrado")
    
    estilo_model = EstilizadoModel(**estilo.model_dump())
    for var, value in estilo_model.__dict__.items(): 
        setattr(db_estilizado, var, value) if value is not None else None

    db.commit()
    db.refresh(db_estilizado)
    return db_estilizado.to_api()

@router.delete("/estilizado/{estilizado_id}", status_code=204)
async def delete_estilizado(estilizado_id: int, db: db_dependency):
    db_estilizado = db.query(models.Estilizado).filter(models.Estilizado.id == estilizado_id).first()
    if db_estilizado is None:
        raise HTTPException(status_code=404, detail="Servicio de estilizado no existe")
    try:
        db.delete(db_estilizado)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return {"detail": "Servicio de estilizado ha sido eliminado"}
