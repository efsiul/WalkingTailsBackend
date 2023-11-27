from db.database    import Base
from sqlalchemy     import Column, Integer, String
from sqlalchemy.orm import relationship

class Mascota(Base):
    __tablename__   = "mascotas"
    id              = Column(Integer, primary_key=True, index=True)
    tipo_mascota    = Column(String)
    raza            = Column(String)
    nombre_mascota  = Column(String)
    edad_mascota    = Column(String)
    observaciones   = Column(String)
    paseos          = relationship("Paseo",      back_populates="mascota")
    enfermerias     = relationship("Enfermeria", back_populates="mascota")
    estilizados     = relationship("Estilizado", back_populates="mascota")