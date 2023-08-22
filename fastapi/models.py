from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship, mapped_column
from database import Base


class Autor(Base):
    __tablename__ = 'autor'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    livros: Mapped[List['Livro']] = relationship(back_populates='autor', cascade='all')

    def __repr__(self) -> str:
        return 'Autor(id=%d, nome=%s)' % (self.id, self.nome)
    

class Livro(Base):
    __tablename__ = 'livro'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(255))
    autor: Mapped['Autor'] = relationship(back_populates='livros')

    def __repr__(self) -> str:
        return 'Livro(id=%d, nome=%s, autor=%s)' % (self.id, self.nome, self.autor)