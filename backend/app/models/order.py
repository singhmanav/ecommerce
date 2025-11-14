from typing import Optional
from datetime import datetime
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship


class OrderStatus(str, Enum):
    """Order status enum"""
    PENDING = "PENDING"
    PAID = "PAID"
    PROCESSING = "PROCESSING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


class Order(SQLModel, table=True):
    """Order model"""
    __tablename__ = "orders"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False, index=True)
    
    # Totals
    subtotal: float = Field(nullable=False)
    tax: float = Field(default=0.0)
    total_amount: float = Field(nullable=False)
    
    # Status
    status: str = Field(default=OrderStatus.PENDING.value)
    
    # Shipping Information
    shipping_name: str = Field(nullable=False)
    shipping_address_line1: str = Field(nullable=False)
    shipping_address_line2: Optional[str] = None
    shipping_city: str = Field(nullable=False)
    shipping_state: str = Field(nullable=False)
    shipping_pincode: str = Field(nullable=False)
    shipping_phone: str = Field(nullable=False)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class OrderItem(SQLModel, table=True):
    """Order item model"""
    __tablename__ = "order_items"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="orders.id", nullable=False, index=True)
    product_id: int = Field(foreign_key="products.id", nullable=False)
    
    # Product details at time of order
    product_name: str = Field(nullable=False)
    product_image: Optional[str] = None
    unit_price: float = Field(nullable=False)
    quantity: int = Field(nullable=False)
    
    # Selected options
    selected_size: Optional[str] = None
    selected_color: Optional[str] = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)