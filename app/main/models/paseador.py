from db.database    import Base
from sqlalchemy     import Column, Integer, String, Date
from sqlalchemy.orm import relationship



class Paseador(Base):
    __tablename__           = "paseadores"
    id                      = Column(Integer, primary_key=True, index=True)
    nombre_completo         = Column(String, index=True)
    apellidos_completos     = Column(String)
    tipo_documento          = Column(String)
    num_documento           = Column(String)
    fecha_nacimiento        = Column(Date)
    num_celular             = Column(Integer)
    email                   = Column(String, unique=True, index=True)
    calificacion_general    = Column(Integer)
    password                = Column(String)
    paseos                  = relationship("Paseo", back_populates="paseador")