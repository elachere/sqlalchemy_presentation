import sqlalchemy

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URI = "mysql+pymysql://etienne:1234@localhost:3399"
DB_NAME = "presentation_db"

engine = sqlalchemy.create_engine(f"{DB_URI}/{DB_NAME}", echo=True)

Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
