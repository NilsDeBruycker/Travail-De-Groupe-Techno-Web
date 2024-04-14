from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey

from my_app.database import Base


class Comment(Base):
    __tablename__ = "comments"
    
    id = mapped_column(String(72), primary_key=True)
    message = mapped_column(String(2048))
    
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    task: Mapped["Task"] = relationship()


class Task(Base):
    __tablename__ = "tasks"
    
    id = mapped_column(String(72), primary_key=True)
    name = mapped_column(String(72))
    description : Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    creation_date = mapped_column(DateTime)
    
    comments: Mapped[list["Comment"]] = relationship()
