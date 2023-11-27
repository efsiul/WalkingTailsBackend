from sqlalchemy                 import create_engine
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE    = 'postgresql://postgres:841205@localhost:5432/walking_tails_db'
engine          = create_engine(URL_DATABASE)
SessionLocal    = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base            = declarative_base()

def create_all_tables(engine):
    Base.metadata.create_all(bind=engine)