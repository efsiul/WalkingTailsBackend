from db.database    import Base
from sqlalchemy     import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class DuenoMascota(Base):
    __tablename__       = "duenos_mascotas"
    id                  = Column(Integer, primary_key=True, index=True)
    nombre_completo     = Column(String, index=True)
    apellidos_completos = Column(String)
    tipo_documento      = Column(String)
    num_documento       = Column(String)
    num_celular         = Column(Integer)
    email               = Column(String, unique=True, index=True)
    password            = Column(String)
    tipo_mascota        = Column(String)
    nombre_mascota      = Column(String)
    id_mascota          = Column(Integer, ForeignKey('mascotas.id'))
    estilizados         = relationship("Estilizado", back_populates="dueno_mascota")