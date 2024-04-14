from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.database import Base
from app.models.book import Book
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey

class User(Base):
    __tablename__ = 'users'
    
    id          : Mapped[str] = mapped_column(String(72), primary_key=True)
    username    : Mapped[str] = mapped_column(String(72), unique=True)
    password    : Mapped[str] = mapped_column(String(72))
    blocked     : Mapped[bool]=mapped_column(bool)
    children: Mapped[list["Book"]] = relationship()
