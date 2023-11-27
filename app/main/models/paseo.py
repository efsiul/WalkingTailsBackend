
from sqlalchemy     import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.database    import Base

class Paseo(Base):
    __tablename__       = "paseos"
    
    id                  = Column(Integer, primary_key=True, index=True)
    lugar_recogida      = Column(String)
    lugar_entrega       = Column(String)
    fecha_hora_recogida = Column(Date)
    fecha_hora_entrega  = Column(Date)
    tiempo_paseo        = Column(Float)
    calificacion        = Column(Integer)
    tarifa_paseo        = Column(Float)
    observaciones       = Column(String)
    id_paseador         = Column(Integer, ForeignKey('paseadores.id'))
    id_mascota          = Column(Integer, ForeignKey('mascotas.id'))
    paseador            = relationship("Paseador",  back_populates="paseos")
    mascota             = relationship("Mascota",   back_populates="paseos")