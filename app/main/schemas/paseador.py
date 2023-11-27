from pydantic import BaseModel, Field
from datetime import date

# Updating EmployeeBase to reflect the new Employee model structure
class PaseadorBase(BaseModel):
    id                      : int    
    nombre_completo         : str
    apellidos_completos     : str
    tipo_documento          : str
    num_documento           : str
    fecha_nacimiento        : date
    num_celular             : int
    email                   : str
    calificacion_general    : int
    password                : str
    paseos                  : list
    
class PaseadorModel(PaseadorBase):
    id: int = Field(..., gt=0)  
    
    class Config:
        orm_mode = True