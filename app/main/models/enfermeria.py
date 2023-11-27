
from sqlalchemy     import Column, Integer, String, Date, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.database    import Base


class Enfermeria(Base):
    __tablename__               = "enfermerias"
    id                          = Column(Integer, primary_key=True, index=True)
    FechaHoraHospitalizacion    = Column(Date)
    se_debe_recoger             = Column(Boolean)
    se_debe_entregar            = Column(Boolean)
    es_hospitalizado            = Column(Boolean)
    tiempo_hospitalizacion      = Column(Float)
    tarifa_enfermeria           = Column(Float)
    tarifa_medicinas            = Column(Float)
    observacion                 = Column(String)
    id_mascota                  = Column(Integer, ForeignKey('mascotas.id'))
    mascota                     = relationship("Mascota", back_populates="enfermerias")