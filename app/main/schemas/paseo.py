from pydantic                   import BaseModel, Field
from datetime                   import date

class PaseoApi(BaseModel):
    id                  : int
    lugar_recogida      : str
    lugar_entrega       : str
    fecha_hora_recogida : date
    fecha_hora_entrega  : date
    tiempo_paseo        : float
    calificacion        : int
    tarifa_paseo        : float
    observaciones       : str
    id_paseador         : int
    id_mascota          : int
    paseador            : str
    
class PaseoModel(BaseModel):
    def to_api(self):
        paseo_data = self.__dict__
        return PaseoApi(**paseo_data)
