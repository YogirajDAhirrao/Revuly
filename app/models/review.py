from typing import Optional, List
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB


class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    text: str
    rating: Optional[int] = None

    clean_text: Optional[str] = None
    is_spam: bool = False

    embedding: Optional[List[float]] = Field(
        default=None,
        sa_column=Column(JSONB)
    )
