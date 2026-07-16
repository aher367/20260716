from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field
from typing import Optional
from database import Base

# ==========================================
# 1. SQLAlchemy Database Model
# ==========================================
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    published_year = Column(Integer, nullable=True)

# ==========================================
# 2. Pydantic Schemas (Validation / Serialization)
# ==========================================
class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Title of the book")
    author: str = Field(..., min_length=1, max_length=100, description="Author of the book")
    description: Optional[str] = Field(None, max_length=500, description="Brief description of the book")
    published_year: Optional[int] = Field(None, ge=0, le=2100, description="Year the book was published")

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    published_year: Optional[int] = Field(None, ge=0, le=2100)

class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "A novel about the American dream",
                "published_year": 1925
            }
        }
