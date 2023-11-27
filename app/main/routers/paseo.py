from fastapi                            import APIRouter, HTTPException, Depends
from typing                             import List, Annotated
from sqlalchemy.orm                     import Session
from app.main.schemas.paseo             import  PaseoApi, PaseoModel
from app.main.dependencies.db_session   import get_db
import app.main.models.paseo            as models

router        = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/paseos/")
async def create_paseo(paseo: PaseoApi, db):
    paseo_db = PaseoModel(**paseo.model_dump()) 
    db.add(paseo_db)
    db.commit()
    return paseo_db.to_api()

@router.get("/paseos/")
async def get_paseos(db):
    paseos = db.query(models.Paseo).all()
    return [p.to_api() for p in paseos] 

@router.get("/paseos/{id}") 
async def get_paseo(id: int, db):
    paseo = db.query(models.Paseo).get(id)
    if not paseo:
        raise HTTPException(404, detail="Paseo no encontrado")
    
    return paseo.to_api()

@router.put("/paseos/{id}")
async def update_paseo(id: int, paseo: PaseoApi, db):
    paseo_db = db.query(models.Paseo).get(id)
    if not paseo_db:  
        raise HTTPException(404, detail="Paseo no encontrado")
    
    paseo_model = PaseoModel(**paseo.model_dump())
    for key, value in paseo_model.__dict__.items():
        setattr(paseo_db, key, value)
    
    db.commit()
    db.refresh(paseo_db)
    return paseo_db.to_api()

@router.delete("/paseos/{id}")
async def delete_paseo(id: int, db):
    paseo = db.query(models.Paseo).get(id)
    if not paseo:
        raise HTTPException(404, detail="Paseo no existe")
    db.delete(paseo)  
    db.commit()
    return {"message": "Paseo eliminado satisfactoriamente"}