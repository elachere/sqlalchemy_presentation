import sqlalchemy

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
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
    name = Column(String(length=255))

    phones = relationship(
        "Phone", backref="user", lazy=True
    )  # lazy=True == lazy="select"


class Phone(Base):
    __tablename__ = "phone_number"

    id = Column(Integer, primary_key=True)
    number = Column(String(length=255))

    user_id = Column(Integer, ForeignKey("user.id"))


Base.metadata.create_all(engine)
