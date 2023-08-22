from database import Base, engine
from models import Autor, Livro

Base.metadata.create_all(bind=engine)