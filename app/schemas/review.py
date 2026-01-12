from typing import Optional
from sqlmodel import SQLModel

class ReviewCreate(SQLModel):
    text: str
    rating: Optional[int] = None

class ReviewView(SQLModel):
    id: int
    text: str
    rating: Optional[int] = None