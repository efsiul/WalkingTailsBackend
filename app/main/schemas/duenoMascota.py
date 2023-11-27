from pydantic import BaseModel, Field

class DuenoMascotaBase(BaseModel):
    id                  : int
    id_usuario          : int
    id_mascota          : int
    mascota             : str
    usuario             : str

class DuenoMascotaModel(DuenoMascotaBase):
    id: int = Field(..., gt=0)  
    class Config:
        orm_mode = True