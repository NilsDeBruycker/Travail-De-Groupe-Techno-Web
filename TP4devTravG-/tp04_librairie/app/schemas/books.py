from pydantic import BaseModel, Field
from typing import Optional

class Book(BaseModel):
    id: str
    name: str = Field(min_length=3, max_length=50)
    Author: str = Field(min_length=3, max_length=50)
    Editor: Optional[str] = Field(min_length=3, max_length=50)
    Prix:float=Field(ge=0)
    Owner:str= Field(min_length=3, max_length=50)
    status:str= Field(min_length=3, max_length=50)