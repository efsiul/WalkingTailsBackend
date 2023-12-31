
from sqlalchemy     import Column, Integer, String, Date, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.database    import Base

class Estilizado(Base):
    __tablename__       = "estilizados"
    id                  = Column(Integer, primary_key=True, index=True)
    fechaHoraEstilizado = Column(Date)
    se_debe_recoger     = Column(Boolean)
    se_debe_entregar    = Column(Boolean)
    tipo_estilizado     = Column(String)
    tarifa_estilizado   = Column(Float)
    calificacion        = Column(Integer)
    observaciones       = Column(String)
    id_mascota          = Column(Integer, ForeignKey('mascotas.id'))
    mascota             = relationship("Mascota", back_populates="estilizados")