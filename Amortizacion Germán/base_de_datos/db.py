from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engie = create_engine('sqlite:///base_de_datos/base_de_datos.db')

Session = sessionmaker(bind=engie)
session = Session()

Base = declarative_base()