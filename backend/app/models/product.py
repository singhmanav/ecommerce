from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Column, JSON


class Product(SQLModel, table=True):
    """Product model for clothing items"""
    __tablename__ = "products"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, index=True)
    description: Optional[str] = None
    price: float = Field(nullable=False)
    category: str = Field(nullable=False, index=True)  # T-Shirts, Jeans, Dresses, etc.
    
    # Store as JSON arrays
    sizes: List[str] = Field(default=[], sa_column=Column(JSON))  # ["S", "M", "L", "XL"]
    colors: List[str] = Field(default=[], sa_column=Column(JSON))  # ["Red", "Blue", "Black"]
    images: List[str] = Field(default=[], sa_column=Column(JSON))  # Image URLs
    
    stock: int = Field(default=0)
    is_active: bool = Field(default=True)
    popularity: int = Field(default=0)  # For sorting by popularity
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)