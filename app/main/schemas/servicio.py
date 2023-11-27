from pydantic import BaseModel, Field

# Updating EmployeeBase to reflect the new Employee model structure
class ServicioBase(BaseModel):
    id              : int
    id_paseo        : int
    id_estilizado   : int
    id_enfermeria   : int
    
class ServicioModel(ServicioBase):
    id: int = Field(..., gt=0)  
    
    class Config:
        orm_mode = True