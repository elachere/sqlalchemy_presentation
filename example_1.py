import sqlalchemy

DB_URI = "mysql+pymysql://etienne:1234@localhost:3399"
DB_NAME = "presentation_db"

engine = sqlalchemy.create_engine(f"{DB_URI}/{DB_NAME}", echo=True)
