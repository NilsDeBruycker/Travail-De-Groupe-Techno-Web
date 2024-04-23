from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey,Boolean,CheckConstraint,Float

from app.database import Base


class User(Base):
    __tablename__ = 'users'
    
    email       : Mapped[str] = mapped_column(String(72), primary_key=True)
    username    : Mapped[str] = mapped_column(String(72))
    password    : Mapped[str] = mapped_column(String(72))
    blocked     : Mapped[Boolean]=mapped_column(Boolean)
    role        : Mapped[str] = mapped_column(String(7))
    books       : Mapped[list["Book"]] = relationship()

class Book(Base):
    __tablename__ = "books"
    
    id = mapped_column(String(72), primary_key=True)
    name = mapped_column(String(72))
    Prix = mapped_column(Float) # pas sur que bon type
    status = mapped_column(String(72),)
    Author=mapped_column(String(72))
    Editor= mapped_column(String(72),nullable=True) #metre optionel
    
    owner_email: Mapped[int] = mapped_column(ForeignKey("users.email"),nullable=True)
    owner: Mapped["User"] = relationship()

    __table_args__ = (
            CheckConstraint('Prix >= 0', name='check_positive_price'),
        )


