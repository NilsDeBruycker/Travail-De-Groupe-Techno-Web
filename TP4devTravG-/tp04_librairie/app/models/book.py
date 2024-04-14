from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey

from app.database import Base
from app.models.users import User

class Book(Base):
    __tablename__ = "books"
    
    id = mapped_column(String(72), primary_key=True)
    name = mapped_column(String(72))
    Prix : Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    status = mapped_column(DateTime)
    
    book_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    book: Mapped["User"] = relationship()
