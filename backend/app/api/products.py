from typing import Optional, List
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select, col, func

from app.db.session import get_session
from app.models.product import Product
from app.schemas.product import ProductResponse, ProductListResponse

router = APIRouter()


@router.get("", response_model=ProductListResponse)
async def list_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    size: Optional[str] = None,
    color: Optional[str] = None,
    sort_by: Optional[str] = Query(None, regex="^(price_asc|price_desc|newest|popularity)$"),
    search: Optional[str] = None,
    session: Session = Depends(get_session)
):
    """Get list of products with filters and pagination"""
    
    # Build base query
    statement = select(Product).where(Product.is_active == True)
    
    # Apply filters
    if category:
        statement = statement.where(Product.category == category)
    
    if min_price is not None:
        statement = statement.where(Product.price >= min_price)
    
    if max_price is not None:
        statement = statement.where(Product.price <= max_price)
    
    if size:
        # Filter products that have this size in their sizes JSON array
        statement = statement.where(col(Product.sizes).contains([size]))
    
    if color:
        # Filter products that have this color in their colors JSON array
        statement = statement.where(col(Product.colors).contains([color]))
    
    if search:
        search_term = f"%{search}%"
        statement = statement.where(
            (Product.name.ilike(search_term)) | 
            (Product.description.ilike(search_term))
        )
    
    # Apply sorting
    if sort_by == "price_asc":
        statement = statement.order_by(Product.price.asc())
    elif sort_by == "price_desc":
        statement = statement.order_by(Product.price.desc())
    elif sort_by == "newest":
        statement = statement.order_by(Product.created_at.desc())
    elif sort_by == "popularity":
        statement = statement.order_by(Product.popularity.desc())
    else:
        statement = statement.order_by(Product.created_at.desc())
    
    # Get total count
    count_statement = select(func.count()).select_from(statement.alias())
    total = session.exec(count_statement).one()
    
    # Apply pagination
    offset = (page - 1) * page_size
    statement = statement.offset(offset).limit(page_size)
    
    # Execute query
    products = session.exec(statement).all()
    
    # Calculate total pages
    total_pages = (total + page_size - 1) // page_size
    
    return {
        "products": products,
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages
    }


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: int,
    session: Session = Depends(get_session)
):
    """Get product by ID"""
    product = session.get(Product, product_id)
    
    if not product or not product.is_active:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    return product