import app.main.models.duenoMascota     as models
from app.utils.jwt                      import create_jwt_token, decode_jwt_token
from fastapi                            import APIRouter, HTTPException, Depends
from typing                             import List, Annotated
from sqlalchemy.orm                     import Session
from app.main.schemas.duenoMascota      import DuenoMascotaBase, DuenoMascotaModel
from app.main.dependencies.db_session   import get_db


router          = APIRouter()
db_dependency   = Annotated[Session, Depends(get_db)]

@router.post("/duenoMascota/", response_model=DuenoMascotaModel)
async def create_duenoMascota(
            duenoMascota: DuenoMascotaBase, 
            db          : db_dependency):
    
    db_duenoMascota = models.DuenoMascota(**duenoMascota.model_dump())
    try:
        db.add(db_duenoMascota)
        db.commit()
        db.refresh(db_duenoMascota)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return db_duenoMascota


@router.get("/duenoMascota/", response_model=List[DuenoMascotaModel])
async def read_duenoMascota(
            db      : db_dependency,
            token   : dict = Depends(decode_jwt_token)):
    
    db_duenoMascota = db.query(models.DuenoMascota).all()
    return db_duenoMascota


@router.get("/duenoMascota/{duenos_mascotas_id}", response_model=DuenoMascotaModel)
async def read_duenoMascota(
            duenos_mascotas_id  : str,
            db                  : db_dependency, 
            token               : dict = Depends(decode_jwt_token)):
    
    db_duenoMascota = db.query(models.DuenoMascota).filter(models.DuenoMascota.id_number == duenos_mascotas_id).first()
    if db_duenoMascota is None:
        raise HTTPException(status_code=404, detail="Dueño de mascota no encontrado")
    return db_duenoMascota


@router.put("/duenoMascota/{duenos_mascotas_id}", response_model=DuenoMascotaModel)
async def update_duenoMascota(
            duenos_mascotas_id  : str,
            dueno               : DuenoMascotaBase, 
            db                  : db_dependency , 
            token               : dict = Depends(decode_jwt_token)):
    
    db_duenoMascota = db.query(models.DuenoMascota).filter(models.DuenoMascota.id == duenos_mascotas_id).first()
    if db_duenoMascota is None:
        raise HTTPException(status_code=404, detail=" Dueño de mascota no encontrado")
    for var, value in vars(dueno).items():
        setattr(db_duenoMascota, var, value) if value is not None else None
    db.commit()
    db.refresh(db_duenoMascota)
    return db_duenoMascota


@router.delete("/duenoMascota/{duenos_mascotas_id}", status_code=204)
async def delete_duenoMascota(
            duenos_mascotas_id  : str,
            db                  : db_dependency,
            token               : dict = Depends(decode_jwt_token)):
    
    db_duenoMascota = db.query(models.DuenoMascota).filter(models.DuenoMascota.id == duenos_mascotas_id).first()
    if db_duenoMascota is None:
        raise HTTPException(status_code=404, detail="El dueño de mascota no existe")
    try:
        db.delete(db_duenoMascota)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return {"detail": "El dueño de mascota ha sido eliminado"}


@router.post("/login/duenoMascota/", response_model=dict)
async def login_duenoMascota(email: str, password: str, db: db_dependency):
    # Verifica las credenciales en la base de datos
    db_duenoMascota = db.query(models.DuenoMascota).filter(models.DuenoMascota.email == email, models.DuenoMascota.password == password).first()
    
    if db_duenoMascota is None:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    # Genera un token JWT y lo devuelve
    jwt_token = create_jwt_token({"sub": str(db_duenoMascota.id), "email": db_duenoMascota.email})
    return {"token": jwt_token}