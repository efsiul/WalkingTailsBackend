from fastapi                            import APIRouter, HTTPException, Depends
from typing                             import List, Annotated
from sqlalchemy.orm                     import Session
from app.main.schemas.paseador          import PaseadorBase, PaseadorModel
from app.main.dependencies.db_session   import get_db
import app.main.models.paseador         as models

router          = APIRouter()
db_dependency   = Annotated[Session, Depends(get_db)]

@router.post("/paseador/", response_model=PaseadorModel)
async def create_paseador(paseador: PaseadorBase, db: db_dependency):
    db_paseador = models.Paseador(**paseador.model_dump())
    try:
        db.add(db_paseador)
        db.commit()
        db.refresh(db_paseador)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return db_paseador

@router.get("/paseador/", response_model=List[PaseadorModel])
async def read_paseador(db: db_dependency):
    db_paseador = db.query(models.Paseador).all()
    return db_paseador

@router.get("/paseador/{paseador_id}", response_model=PaseadorModel)
async def read_paseador(paseador_id: str, db: db_dependency):
    db_paseador = db.query(models.Paseador).filter(models.Paseador.id_number == paseador_id).first()
    if db_paseador is None:
        raise HTTPException(status_code=404, detail="Paseador no encontrado")
    return db_paseador

@router.put("/paseador/{paseador_id}", response_model=PaseadorModel)
async def update_paseador(paseador_id: str, paseador: PaseadorBase, db: db_dependency):
    db_paseador = db.query(models.Paseador).filter(models.Paseador.id == paseador_id).first()
    if db_paseador is None:
        raise HTTPException(status_code=404, detail="Paseador no encontrado")
    for var, value in vars(paseador).items():
        setattr(db_paseador, var, value) if value is not None else None
    db.commit()
    db.refresh(db_paseador)
    return db_paseador

@router.delete("/paseador/{paseador_id}", status_code=204)
async def delete_paseador(paseador_id: str, db: db_dependency):
    db_paseador = db.query(models.Paseador).filter(models.Paseador.id == paseador_id).first()
    if db_paseador is None:
        raise HTTPException(status_code=404, detail="El paseador no existe")
    try:
        db.delete(db_paseador)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return {"detail": "El paseador ha sido eliminado"}

# Don't forget to handle exceptions and validate data as needed.