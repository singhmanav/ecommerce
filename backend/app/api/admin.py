from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.core.security import get_current_admin_user
from app.db.session import get_session
from app.models.user import User
from app.models.product import Product
from app.models.order import Order, OrderItem
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.schemas.order import OrderResponse, OrderListResponse, OrderDetailResponse, OrderItemResponse
from datetime import datetime

router = APIRouter()


# Product Management
@router.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_data: ProductCreate,
    current_admin: User = Depends(get_current_admin_user),
    session: Session = Depends(get_session)
):
    """Create a new product (Admin only)"""
    product = Product(**product_data.model_dump())
    
    session.add(product)
    session.commit()
    session.refresh(product)
    
    return product


@router.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    product_data: ProductUpdate,
    current_admin: User = Depends(get_current_admin_user),
    session: Session = Depends(get_session)
):
    """Update a product (Admin only)"""
    product = session.get(Product, product_id)
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    # Update fields
    update_data = product_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(product, key, value)
    
    product.updated_at = datetime.utcnow()
    
    session.add(product)
    session.commit()
    session.refresh(product)
    
    return product


@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
    current_admin: User = Depends(get_current_admin_user),
    session: Session = Depends(get_session)
):
    """Delete a product (Admin only)"""
    product = session.get(Product, product_id)
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    # Soft delete by setting is_active to False
    product.is_active = False
    session.add(product)
    session.commit()
    
    return None


# Order Management
@router.get("/orders", response_model=OrderListResponse)
async def list_all_orders(
    current_admin: User = Depends(get_current_admin_user),
    session: Session = Depends(get_session)
):
    """Get list of all orders (Admin only)"""
    statement = select(Order).order_by(Order.created_at.desc())
    orders = session.exec(statement).all()
    
    return {
        "orders": orders,
        "total": len(orders)
    }


@router.get("/orders/{order_id}", response_model=OrderDetailResponse)
async def get_order_detail(
    order_id: int,
    current_admin: User = Depends(get_current_admin_user),
    session: Session = Depends(get_session)
):
    """Get order details (Admin only)"""
    order = session.get(Order, order_id)
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    # Get order items
    statement = select(OrderItem).where(OrderItem.order_id == order_id)
    items = session.exec(statement).all()
    
    return OrderDetailResponse(
        **order.model_dump(),
        items=[OrderItemResponse(**item.model_dump()) for item in items]
    )