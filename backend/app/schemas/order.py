from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


# Request schemas
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    selected_size: Optional[str] = None
    selected_color: Optional[str] = None


class ShippingAddress(BaseModel):
    shipping_name: str
    shipping_address_line1: str
    shipping_address_line2: Optional[str] = None
    shipping_city: str
    shipping_state: str
    shipping_pincode: str
    shipping_phone: str


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
    shipping_address: ShippingAddress


# Response schemas
class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str
    product_image: Optional[str] = None
    unit_price: float
    quantity: int
    selected_size: Optional[str] = None
    selected_color: Optional[str] = None
    
    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    user_id: int
    subtotal: float
    tax: float
    total_amount: float
    status: str
    shipping_name: str
    shipping_address_line1: str
    shipping_address_line2: Optional[str] = None
    shipping_city: str
    shipping_state: str
    shipping_pincode: str
    shipping_phone: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class OrderDetailResponse(OrderResponse):
    items: List[OrderItemResponse] = []


class OrderListResponse(BaseModel):
    orders: List[OrderResponse]
    total: int