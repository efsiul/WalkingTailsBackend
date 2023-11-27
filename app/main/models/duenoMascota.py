from db.database    import Base
from sqlalchemy     import  Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class DuenoMascota(Base):
    __tablename__       = "duenos_mascotas"
    id                  = Column(Integer,  primary_key=True, index=True)
    id_usuario          = Column(Integer, ForeignKey('usuarios.id'))
    id_mascota          = Column(Integer, ForeignKey('mascotas.id'))
    mascota             = relationship("Mascota", back_populates="dueno_mascota")
    usuario             = relationship("Usuario", back_populates="dueno_mascota", uselist=False)