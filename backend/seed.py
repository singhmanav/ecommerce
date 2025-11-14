"""
Seed script to populate the database with initial data
Run this script to add sample products and an admin user
"""
import asyncio
from sqlmodel import Session

from app.db.session import engine, init_db
from app.models.user import User
from app.models.product import Product
from app.core.security import get_password_hash


def seed_database():
    """Seed database with initial data"""
    
    # Initialize database
    init_db()
    
    with Session(engine) as session:
        # Create admin user
        admin = User(
            email="admin@example.com",
            password_hash=get_password_hash("admin123"),
            full_name="Admin User",
            phone="+1234567890",
            is_admin=True
        )
        session.add(admin)
        
        # Create regular test user
        user = User(
            email="user@example.com",
            password_hash=get_password_hash("user123"),
            full_name="Test User",
            phone="+1234567891"
        )
        session.add(user)
        
        # Create sample products
        products = [
            # T-Shirts
            Product(
                name="Classic White T-Shirt",
                description="Comfortable cotton t-shirt perfect for everyday wear",
                price=499.00,
                category="T-Shirts",
                sizes=["S", "M", "L", "XL", "XXL"],
                colors=["White", "Black", "Grey"],
                images=[
                    "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500",
                    "https://images.unsplash.com/photo-1527719327859-c6ce80353573?w=500"
                ],
                stock=100,
                popularity=50
            ),
            Product(
                name="Graphic Print T-Shirt",
                description="Trendy graphic print t-shirt with modern design",
                price=799.00,
                category="T-Shirts",
                sizes=["S", "M", "L", "XL"],
                colors=["Black", "Navy", "Red"],
                images=[
                    "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500"
                ],
                stock=75,
                popularity=80
            ),
            Product(
                name="V-Neck T-Shirt",
                description="Stylish v-neck t-shirt for a smart casual look",
                price=599.00,
                category="T-Shirts",
                sizes=["S", "M", "L", "XL"],
                colors=["White", "Black", "Grey", "Navy"],
                images=[
                    "https://images.unsplash.com/photo-1581655353564-df123a1eb820?w=500"
                ],
                stock=60,
                popularity=40
            ),
            
            # Shirts
            Product(
                name="Formal White Shirt",
                description="Classic formal shirt perfect for office and events",
                price=1299.00,
                category="Shirts",
                sizes=["S", "M", "L", "XL", "XXL"],
                colors=["White", "Light Blue", "Pink"],
                images=[
                    "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=500"
                ],
                stock=50,
                popularity=70
            ),
            Product(
                name="Casual Denim Shirt",
                description="Comfortable denim shirt for casual outings",
                price=1499.00,
                category="Shirts",
                sizes=["S", "M", "L", "XL"],
                colors=["Blue", "Dark Blue", "Light Blue"],
                images=[
                    "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500"
                ],
                stock=40,
                popularity=60
            ),
            Product(
                name="Checkered Casual Shirt",
                description="Stylish checkered pattern shirt for weekend wear",
                price=1199.00,
                category="Shirts",
                sizes=["S", "M", "L", "XL"],
                colors=["Red", "Blue", "Green"],
                images=[
                    "https://images.unsplash.com/photo-1603252109303-2751441dd157?w=500"
                ],
                stock=55,
                popularity=45
            ),
            
            # Jeans
            Product(
                name="Slim Fit Blue Jeans",
                description="Modern slim fit jeans with stretch fabric",
                price=1999.00,
                category="Jeans",
                sizes=["28", "30", "32", "34", "36"],
                colors=["Blue", "Dark Blue", "Black"],
                images=[
                    "https://images.unsplash.com/photo-1542272604-787c3835535d?w=500"
                ],
                stock=80,
                popularity=90
            ),
            Product(
                name="Relaxed Fit Jeans",
                description="Comfortable relaxed fit jeans for all-day comfort",
                price=1799.00,
                category="Jeans",
                sizes=["28", "30", "32", "34", "36", "38"],
                colors=["Blue", "Light Blue", "Grey"],
                images=[
                    "https://images.unsplash.com/photo-1604176354204-9268737828e4?w=500"
                ],
                stock=70,
                popularity=55
            ),
            Product(
                name="Skinny Fit Black Jeans",
                description="Sleek skinny fit jeans in classic black",
                price=2199.00,
                category="Jeans",
                sizes=["28", "30", "32", "34", "36"],
                colors=["Black", "Dark Grey"],
                images=[
                    "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=500"
                ],
                stock=65,
                popularity=85
            ),
            
            # Dresses
            Product(
                name="Summer Floral Dress",
                description="Light and breezy floral dress perfect for summer",
                price=1899.00,
                category="Dresses",
                sizes=["XS", "S", "M", "L", "XL"],
                colors=["Floral Pink", "Floral Blue", "Floral Yellow"],
                images=[
                    "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=500"
                ],
                stock=45,
                popularity=75
            ),
            Product(
                name="Elegant Evening Dress",
                description="Sophisticated evening dress for special occasions",
                price=3499.00,
                category="Dresses",
                sizes=["XS", "S", "M", "L"],
                colors=["Black", "Navy", "Maroon"],
                images=[
                    "https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=500"
                ],
                stock=30,
                popularity=65
            ),
            Product(
                name="Casual Midi Dress",
                description="Versatile midi dress for everyday elegance",
                price=1599.00,
                category="Dresses",
                sizes=["XS", "S", "M", "L", "XL"],
                colors=["Red", "Blue", "Green", "Black"],
                images=[
                    "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=500"
                ],
                stock=50,
                popularity=70
            ),
            
            # Jackets
            Product(
                name="Leather Biker Jacket",
                description="Classic leather jacket with modern styling",
                price=4999.00,
                category="Jackets",
                sizes=["S", "M", "L", "XL"],
                colors=["Black", "Brown"],
                images=[
                    "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=500"
                ],
                stock=25,
                popularity=80
            ),
            Product(
                name="Denim Jacket",
                description="Timeless denim jacket for layering",
                price=2499.00,
                category="Jackets",
                sizes=["S", "M", "L", "XL", "XXL"],
                colors=["Blue", "Black", "Light Blue"],
                images=[
                    "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=500"
                ],
                stock=40,
                popularity=75
            ),
            Product(
                name="Windbreaker Jacket",
                description="Lightweight windbreaker for outdoor activities",
                price=1999.00,
                category="Jackets",
                sizes=["S", "M", "L", "XL"],
                colors=["Black", "Navy", "Red", "Green"],
                images=[
                    "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=500"
                ],
                stock=60,
                popularity=60
            ),
        ]
        
        for product in products:
            session.add(product)
        
        # Commit all changes
        session.commit()
        
        print("✅ Database seeded successfully!")
        print(f"   - Created admin user: admin@example.com / admin123")
        print(f"   - Created test user: user@example.com / user123")
        print(f"   - Created {len(products)} sample products")


if __name__ == "__main__":
    seed_database()