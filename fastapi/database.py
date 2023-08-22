from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///db.sqlite3', echo=True)
session = sessionmaker(autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_database():
    db = session()
    try:
        yield db
    finally:
        db.close()