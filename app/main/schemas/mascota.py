from pydantic import BaseModel, Field


# Updating EmployeeBase to reflect the new Employee model structure
class MascotaBase(BaseModel):
    
    id              : int
    tipo_mascota    : str
    raza            : str
    nombre_mascota  : str
    edad_mascota    : str
    observaciones   : str
    enfermerias     : list
    
class MascotaModel(MascotaBase):
    id: int = Field(..., gt=0)  
    
    class Config:
        orm_mode = True