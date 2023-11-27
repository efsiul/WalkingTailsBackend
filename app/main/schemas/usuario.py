from pydantic import BaseModel, Field
from datetime import date

# Updating EmployeeBase to reflect the new Employee model structure
class UsuarioBase(BaseModel):
    id                      : int    
    nombre_completo         : str
    apellidos_completos     : str
    tipo_documento          : str
    num_documento           : str
    num_celular             : int
    fecha_nacimiento        : date
    email                   : str
    password                : str
    tipo_usuario            : str

    paseador                : str
    dueno_mascota           : str
        
class UsuarioModel(UsuarioBase):
    id: int = Field(..., gt=0)  
    
    class Config:
        orm_mode = True