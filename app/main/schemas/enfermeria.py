from pydantic                   import BaseModel
from datetime                   import date

class EnfermeriaApi(BaseModel):
    id                          : int
    FechaHoraHospitalizacion    : date
    se_debe_recoger             : bool
    se_debe_entregar            : bool
    es_hospitalizado            : bool
    tiempo_hospitalizacion      : float
    tarifa_enfermeria           : float
    tarifa_medicinas            : float
    observacion                 : str
    id_mascota                  : int
    mascota                     : str

class EnfermeriaModel(BaseModel):
    def to_api(self):
        enfermeria_data = self.__dict__
        return EnfermeriaApi(**enfermeria_data)