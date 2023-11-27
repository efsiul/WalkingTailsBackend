from pydantic                   import BaseModel
from datetime                   import date
from app.main.models.estilizado import Estilizado

# Updating EmployeeBase to reflect the new Employee model structure
class EstilizadoApi(BaseModel):
    id                  : int
    fechaHoraEstilizado : date
    se_debe_recoger     : bool
    se_debe_entregar    : bool
    tipo_estilizado     : str
    tarifa_estilizado   : float
    calificacion        : int
    observaciones       : str
    id_mascota          : int
    mascota             : str
    
class EstilizadoModel(BaseModel):
    def to_api(self):
        estilizado_data = self.__dict__
        return EstilizadoApi(**estilizado_data)
