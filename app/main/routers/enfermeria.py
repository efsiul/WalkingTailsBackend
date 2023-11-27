from fastapi                            import APIRouter, HTTPException, Depends
from typing                             import List, Annotated
from sqlalchemy.orm                     import Session
from app.main.schemas.enfermeria        import EnfermeriaApi, EnfermeriaModel
from app.main.dependencies.db_session   import get_db
import app.main.models.enfermeria       as models

router          = APIRouter()
db_dependency   = Annotated[Session, Depends(get_db)]

@router.post("/enfermeria/", response_model=EnfermeriaModel)
async def create_enfermeria(enfermeria: EnfermeriaApi, db: db_dependency):
    db_enfermeria = models.Enfermeria(**enfermeria.model_dump())
    try:
        db.add(db_enfermeria)
        db.commit()
        db.refresh(db_enfermeria)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return db_enfermeria.to_api()

@router.get("/enfermeria/", response_model=List[EnfermeriaModel])
async def read_enfermeria(db: db_dependency):
    db_enfermerias = db.query(models.Enfermeria).all()
    return [enfermeria.to_api() for enfermeria in db_enfermerias]

@router.get("/enfermeria/{enfermeria_id}", response_model=EnfermeriaModel)
async def read_enfermeria(enfermeria_id: int, db: db_dependency):
    db_enfermeria = db.query(models.Enfermeria).filter(models.Enfermeria.id == enfermeria_id).first()
    if db_enfermeria is None:
        raise HTTPException(status_code=404, detail="Servicio de enfermería no encontrado")
    return db_enfermeria.to_api()

@router.put("/enfermeria/{enfermeria_id}", response_model=EnfermeriaModel)
async def update_enfermeria(enfermeria_id: int, enfermeria: EnfermeriaApi, db: db_dependency):
    db_enfermeria = db.query(models.Enfermeria).filter(models.Enfermeria.id == enfermeria_id).first()
    if db_enfermeria is None:
        raise HTTPException(status_code=404, detail="Servicio de enfermería no encontrado")
    
    enfermeria_model = EnfermeriaModel(**enfermeria.model_dump())
    for var, value in enfermeria_model.__dict__.items():
        setattr(db_enfermeria, var, value) if value is not None else None

    db.commit()
    db.refresh(db_enfermeria)
    return db_enfermeria.to_api()

@router.delete("/enfermeria/{enfermeria_id}", status_code=204)
async def delete_enfermeria(enfermeria_id: int, db: db_dependency):
    db_enfermeria = db.query(models.Enfermeria).filter(models.Enfermeria.id == enfermeria_id).first()
    if db_enfermeria is None:
        raise HTTPException(status_code=404, detail="Servicio de enfermería no existe")
    try:
        db.delete(db_enfermeria)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return {"detail": "Servicio de enfermería ha sido eliminado"}
