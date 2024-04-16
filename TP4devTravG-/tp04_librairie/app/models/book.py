from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey,Boolean

from app.database import Base

class Book(Base):
    __tablename__ = "books"
    
    id = mapped_column(String(72), primary_key=True)
    name = mapped_column(String(72))
    Prix : Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    status = mapped_column(DateTime)
    
    owner_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    owner: Mapped["User"] = relationship()

class User(Base):
    __tablename__ = 'users'
    
    id          : Mapped[str] = mapped_column(String(72), primary_key=True)
    username    : Mapped[str] = mapped_column(String(72), unique=True)
    password    : Mapped[str] = mapped_column(String(72))
    blocked     : Mapped[Boolean]=mapped_column(Boolean)
    role        : Mapped[str] = mapped_column(String(7))
    books: Mapped[list["Book"]] = relationship()
