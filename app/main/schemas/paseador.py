from pydantic import BaseModel, Field
from datetime import date

# Updating EmployeeBase to reflect the new Employee model structure
class PaseadorBase(BaseModel):
    id                      : int
    id_usuario              : int    
    calificacion_general    : int
    id_mascota              : int
    paseos                  : list
    mascota                 : str
    usuario                 : str
    
class PaseadorModel(PaseadorBase):
    id: int = Field(..., gt=0)  
    
    class Config:
        orm_mode = True