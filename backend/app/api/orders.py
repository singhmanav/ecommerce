from typing import List
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.core.security import get_current_user
from app.db.session import get_session
from app.models.user import User
from app.models.order import Order, OrderItem, OrderStatus
from app.models.product import Product
from app.schemas.order import (
    OrderCreate,
    OrderResponse,
    OrderDetailResponse,
    OrderListResponse,
    OrderItemResponse
)

router = APIRouter()


@router.post("", response_model=OrderDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
    order_data: OrderCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Create a new order"""
    
    if not order_data.items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Order must contain at least one item"
        )
    
    # Calculate totals and validate products
    subtotal = 0.0
    order_items_data = []
    
    for item in order_data.items:
        # Get product
        product = session.get(Product, item.product_id)
        
        if not product or not product.is_active:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product {item.product_id} not found"
            )
        
        # Validate stock
        if product.stock < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product {product.name}"
            )
        
        # Validate size
        if item.selected_size and item.selected_size not in product.sizes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid size {item.selected_size} for product {product.name}"
            )
        
        # Validate color
        if item.selected_color and item.selected_color not in product.colors:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid color {item.selected_color} for product {product.name}"
            )
        
        # Calculate item total
        item_total = product.price * item.quantity
        subtotal += item_total
        
        # Store order item data
        order_items_data.append({
            "product": product,
            "quantity": item.quantity,
            "selected_size": item.selected_size,
            "selected_color": item.selected_color,
            "unit_price": product.price
        })
    
    # Calculate tax (simple 18% tax for demo)
    tax = subtotal * 0.18
    total_amount = subtotal + tax
    
    # Create order
    order = Order(
        user_id=current_user.id,
        subtotal=subtotal,
        tax=tax,
        total_amount=total_amount,
        status=OrderStatus.PAID.value,  # Mock payment - assume paid
        shipping_name=order_data.shipping_address.shipping_name,
        shipping_address_line1=order_data.shipping_address.shipping_address_line1,
        shipping_address_line2=order_data.shipping_address.shipping_address_line2,
        shipping_city=order_data.shipping_address.shipping_city,
        shipping_state=order_data.shipping_address.shipping_state,
        shipping_pincode=order_data.shipping_address.shipping_pincode,
        shipping_phone=order_data.shipping_address.shipping_phone
    )
    
    session.add(order)
    session.commit()
    session.refresh(order)
    
    # Create order items and update stock
    order_items = []
    for item_data in order_items_data:
        product = item_data["product"]
        
        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            product_name=product.name,
            product_image=product.images[0] if product.images else None,
            unit_price=item_data["unit_price"],
            quantity=item_data["quantity"],
            selected_size=item_data["selected_size"],
            selected_color=item_data["selected_color"]
        )
        
        session.add(order_item)
        order_items.append(order_item)
        
        # Update product stock
        product.stock -= item_data["quantity"]
        product.popularity += item_data["quantity"]  # Increase popularity
        session.add(product)
    
    session.commit()
    
    # Refresh order items
    for order_item in order_items:
        session.refresh(order_item)
    
    # Return order with items
    return OrderDetailResponse(
        **order.model_dump(),
        items=[OrderItemResponse(**item.model_dump()) for item in order_items]
    )


@router.get("", response_model=OrderListResponse)
async def list_orders(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get list of orders for current user"""
    statement = select(Order).where(Order.user_id == current_user.id).order_by(Order.created_at.desc())
    orders = session.exec(statement).all()
    
    return {
        "orders": orders,
        "total": len(orders)
    }


@router.get("/{order_id}", response_model=OrderDetailResponse)
async def get_order(
    order_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get order details"""
    order = session.get(Order, order_id)
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    # Check if order belongs to current user
    if order.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this order"
        )
    
    # Get order items
    statement = select(OrderItem).where(OrderItem.order_id == order_id)
    items = session.exec(statement).all()
    
    return OrderDetailResponse(
        **order.model_dump(),
        items=[OrderItemResponse(**item.model_dump()) for item in items]
    )