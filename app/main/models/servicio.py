from db.database    import Base
from sqlalchemy     import Column, Integer, String,  ForeignKey



class Servicio(Base):
    __tablename__   = "servicios"
    id              = Column(Integer, primary_key=True, index=True)
    id_paseo        = Column(Integer, ForeignKey('paseadores.id'))
    id_estilizado   = Column(Integer, ForeignKey('duenos_mascotas.id'))
    id_enfermeria   = Column(Integer, ForeignKey('mascotas.id'))