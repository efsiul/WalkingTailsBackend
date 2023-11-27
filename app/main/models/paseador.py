from db.database    import Base
from sqlalchemy     import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship



class Paseador(Base):
    __tablename__           = "paseadores"
    id                      = Column(Integer,  primary_key=True, index=True)
    id_usuario              = Column(Integer, ForeignKey('usuarios.id'))
    calificacion_general    = Column(Integer)
    id_mascota              = Column(Integer, ForeignKey('mascotas.id'))
    paseos                  = relationship("Paseo",     back_populates="paseador")
    mascota                 = relationship("Mascota",   back_populates="paseador")
    usuario                 = relationship("Usuario",   back_populates="paseador", uselist=False)