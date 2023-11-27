from fastapi                            import APIRouter, HTTPException, Depends
from typing                             import List, Annotated
from sqlalchemy.orm                     import Session
from app.main.schemas.mascota           import MascotaBase, MascotaModel
from app.main.dependencies.db_session   import get_db
import app.main.models.mascota          as models

router          = APIRouter()
db_dependency   = Annotated[Session, Depends(get_db)]

@router.post("/mascota/", response_model=MascotaModel)
async def create_mascota(mascota: MascotaBase, db: db_dependency):
    db_mascota = models.Mascota(**mascota.model_dump())
    try:
        db.add(db_mascota)
        db.commit()
        db.refresh(db_mascota)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return db_mascota

@router.get("/mascota/", response_model=List[MascotaModel])
async def read_mascota(db: db_dependency):
    db_mascota = db.query(models.Mascota).all()
    return db_mascota

@router.get("/mascota/{mascota_id}", response_model=MascotaModel)
async def read_mascota(mascota_id: str, db: db_dependency):
    db_mascota = db.query(models.Mascota).filter(models.Mascota.id_number == mascota_id).first()
    if db_mascota is None:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return db_mascota

@router.put("/mascota/{mascota_id}", response_model=MascotaModel)
async def update_mascota(mascota_id: str, mascota: MascotaBase, db: db_dependency):
    db_mascota = db.query(models.Mascota).filter(models.Mascota.id == mascota_id).first()
    if db_mascota is None:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    for var, value in vars(mascota).items():
        setattr(db_mascota, var, value) if value is not None else None
    db.commit()
    db.refresh(db_mascota)
    return db_mascota

@router.delete("/mascota/{mascota_id}", status_code=204)
async def delete_mascota(mascota_id: str, db: db_dependency):
    db_mascota = db.query(models.Mascota).filter(models.Mascota.id == mascota_id).first()
    if db_mascota is None:
        raise HTTPException(status_code=404, detail="La mascota no existe")
    try:
        db.delete(db_mascota)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return {"detail": "La mascota ha sido eliminado"}

# Don't forget to handle exceptions and validate data as needed.