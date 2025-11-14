from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


# Request schemas
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category: str
    sizes: List[str] = []
    colors: List[str] = []
    images: List[str] = []
    stock: int = 0


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    sizes: Optional[List[str]] = None
    colors: Optional[List[str]] = None
    images: Optional[List[str]] = None
    stock: Optional[int] = None
    is_active: Optional[bool] = None


# Response schemas
class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    category: str
    sizes: List[str]
    colors: List[str]
    images: List[str]
    stock: int
    is_active: bool
    popularity: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    products: List[ProductResponse]
    total: int
    page: int
    page_size: int
    total_pages: int