from typing import Optional, List
from sqlmodel import SQLModel

class ReviewCreate(SQLModel):
    text: str
    rating: Optional[int] = None

class ReviewView(SQLModel):
    id: int
    text: str
    rating: Optional[int] = None

class ReviewFilterResponse(SQLModel):
    query: str
    exclude: Optional[List[str]] = []
    threshold: float = 0.60
    top_k: int = 5    