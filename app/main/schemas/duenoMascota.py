from pydantic import BaseModel, Field

class DuenoMascotaBase(BaseModel):
    id                  : str
    nombre_completo     : str
    apellidos_completos : str
    tipo_documento      : str
    num_documento       : str
    num_celular         : int
    email               : str
    password            : str
    tipo_mascota        : str
    nombre_mascota      : str
    id_mascota          : int
    estilizados         : list
    

class DuenoMascotaModel(DuenoMascotaBase):
    id: int = Field(..., gt=0)  
    class Config:
        orm_mode = True