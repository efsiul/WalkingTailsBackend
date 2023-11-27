# app.main.routers.usuario.py
import app.main.models.usuario          as models
from fastapi                            import APIRouter, HTTPException, Depends
from typing                             import List, Annotated
from sqlalchemy.orm                     import Session
from app.main.schemas.usuario           import UsuarioBase, UsuarioModel
from app.main.dependencies.db_session   import get_db
from app.utils.jwt import decode_jwt_token

router          = APIRouter()
db_dependency   = Annotated[Session, Depends(get_db)]

@router.post("/usuario/", response_model=UsuarioModel)
async def create_usuario(usuario: UsuarioBase, db: db_dependency):
    db_usuario = models.Usuario(**usuario.model_dump())
    try:
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return db_usuario



@router.get("/usuario/", response_model=List[UsuarioModel])
async def read_usuarios(
            db      : db_dependency,
            token   : dict = Depends(decode_jwt_token)):
    db_usuarios = db.query(models.Usuario).all()
    return db_usuarios



@router.get("/usuario/{usuario_id}", response_model=UsuarioModel)
async def read_usuario(
            usuario_id  : str,
            db          : db_dependency,
            token       : dict = Depends(decode_jwt_token)):
    
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_number == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario



@router.put("/usuario/{usuario_id}", response_model=UsuarioModel)
async def update_usuario(
            usuario_id  : str, 
            usuario     : UsuarioBase, 
            db          : db_dependency, 
            token       : dict = Depends(decode_jwt_token)):
    
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for var, value in vars(usuario).items():
        setattr(db_usuario, var, value) if value is not None else None
    db.commit()
    db.refresh(db_usuario)
    return db_usuario



@router.delete("/usuario/{usuario_id}", status_code=204)
async def delete_usuario(
            usuario_id  : str,
            db          : db_dependency,
            token       : dict = Depends(decode_jwt_token)):
    
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    try:
        db.delete(db_usuario)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return {"detail": "El usuario ha sido eliminado"}
