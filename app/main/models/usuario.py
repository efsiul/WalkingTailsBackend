
from sqlalchemy     import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database    import Base

class Usuario(Base):
    __tablename__       = "usuarios"
    id                  = Column(Integer, primary_key=True, index=True)
    nombre_completo     = Column(String, index=True)
    apellidos_completos = Column(String)
    tipo_documento      = Column(String)
    num_documento       = Column(String)
    num_celular         = Column(Integer)
    fecha_nacimiento    = Column(Date)
    email               = Column(String, unique=True, index=True)
    password            = Column(String)
    tipo_usuario        = Column(String)
    
    paseador            = relationship("Paseador",      back_populates="usuario", uselist=False)
    dueno_mascota       = relationship("DuenoMascota",  back_populates="usuario", uselist=False)