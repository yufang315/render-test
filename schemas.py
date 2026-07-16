from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    published_year: Optional[int] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    published_year: Optional[int] = None

class BookResponse(BookBase):
    id: int

    class Config:
        # Pydantic v2 uses from_attributes=True, v1 uses orm_mode=True.
        # We define both for compatibility.
        from_attributes = True
        orm_mode = True
