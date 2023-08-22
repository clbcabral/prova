from sqlalchemy.orm import Session
from models import Autor, Livro


class AutorRepository:
    
    @staticmethod
    def find_all(db: Session):
        return db.query(Autor).all()