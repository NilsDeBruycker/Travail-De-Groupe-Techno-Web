from pydantic import BaseModel, Field
from typing import Optional

class Book(BaseModel):
    id: str
    name: str = Field(min_length=3, max_length=50)
    Author: str = Field(min_length=3, max_length=50)
    Editor: Optional[str] = Field(min_length=3, max_length=50)