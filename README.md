# E-Commerce Clothing Store

A full-stack e-commerce web application for clothing built with FastAPI (Python) backend and Next.js (React, TypeScript) frontend.

## 🚀 Features

### User Features
- **Product Catalog**: Browse products with filters (category, price, size, color) and sorting
- **Product Details**: View detailed product information with multiple images
- **Shopping Cart**: Add products, update quantities, and manage cart items
- **User Authentication**: Register and login with email/password (JWT-based)
- **Checkout**: Complete purchase with shipping address form
- **Order History**: View past orders and track status
- **Responsive Design**: Works seamlessly on desktop and mobile devices

### Admin Features
- **Product Management**: Create, update, and delete products
- **Order Management**: View all orders and their details
- **Admin Dashboard**: Centralized management interface

### Technical Features
- **RESTful API**: Clean JSON API design
- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: Bcrypt for secure password storage
- **Database**: PostgreSQL with SQLModel ORM
- **Type Safety**: TypeScript on frontend, Pydantic schemas on backend
- **Modern UI**: Tailwind CSS for responsive, beautiful design

## 📋 Prerequisites

- Python 3.9+
- Node.js 18+
- PostgreSQL 14+
- npm or yarn

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ecomerce-app
```

### 2. Backend Setup

#### Install Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and configure:
- `DATABASE_URL`: Your PostgreSQL connection string
- `SECRET_KEY`: A secure random string for JWT signing

Example:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ecommerce_db
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
FRONTEND_URL=http://localhost:3000
DEBUG=True
```

#### Create Database

```bash
# Using PostgreSQL CLI
createdb ecommerce_db

# Or using psql
psql -U postgres
CREATE DATABASE ecommerce_db;
\q
```

#### Seed Database (Optional but Recommended)

This will create sample products and test users:

```bash
python seed.py
```

**Test Accounts Created:**
- Admin: `admin@example.com` / `admin123`
- User: `user@example.com` / `user123`

#### Run Backend Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

### 3. Frontend Setup

#### Install Dependencies

```bash
cd frontend
npm install
```

#### Configure Environment

```bash
cp .env.example .env.local
```

Edit `.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

#### Run Frontend Development Server

```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## 🐳 Docker Setup (Alternative)

You can run the entire stack with Docker Compose:

```bash
docker-compose up -d
```

This will start:
- PostgreSQL on port 5432
- Backend API on port 8000
- Frontend on port 3000

To seed the database with Docker:

```bash
docker-compose exec backend python seed.py
```

## 📁 Project Structure

```
ecommerce-app/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── api/               # API routes
│   │   │   ├── auth.py        # Authentication endpoints
│   │   │   ├── products.py    # Product endpoints
│   │   │   ├── orders.py      # Order endpoints
│   │   │   └── admin.py       # Admin endpoints
│   │   ├── core/              # Core configuration
│   │   │   ├── config.py      # Settings
│   │   │   └── security.py    # Security utilities
│   │   ├── db/                # Database
│   │   │   └── session.py     # DB session management
│   │   ├── models/            # SQLModel models
│   │   │   ├── user.py
│   │   │   ├── product.py
│   │   │   └── order.py
│   │   ├── schemas/           # Pydantic schemas
│   │   │   ├── user.py
│   │   │   ├── product.py
│   │   │   └── order.py
│   │   └── main.py            # FastAPI app
│   ├── seed.py                # Database seeding script
│   ├── requirements.txt       # Python dependencies
│   └── .env.example           # Environment template
│
├── frontend/                   # Next.js frontend
│   ├── app/                   # Next.js 14 App Router
│   │   ├── auth/              # Auth pages
│   │   ├── products/          # Product pages
│   │   ├── cart/              # Cart page
│   │   ├── checkout/          # Checkout page
│   │   ├── orders/            # Order pages
│   │   ├── admin/             # Admin pages
│   │   ├── layout.tsx         # Root layout
│   │   └── page.tsx           # Home page
│   ├── components/            # React components
│   │   ├── Header.tsx
│   │   ├── Footer.tsx
│   │   └── ProductCard.tsx
│   ├── lib/                   # Utilities
│   │   ├── api.ts             # API functions
│   │   ├── api-client.ts      # API client
│   │   └── auth-context.tsx   # Auth context
│   ├── types/                 # TypeScript types
│   │   └── index.ts
│   ├── package.json
│   └── .env.example           # Environment template
│
├── docker-compose.yml          # Docker composition
└── README.md                   # This file
```

## 🔑 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user

### Products
- `GET /api/products` - List products (with filters)
- `GET /api/products/{id}` - Get product detail

### Orders
- `POST /api/orders` - Create order
- `GET /api/orders` - List user's orders
- `GET /api/orders/{id}` - Get order detail

### Admin
- `POST /api/admin/products` - Create product
- `PUT /api/admin/products/{id}` - Update product
- `DELETE /api/admin/products/{id}` - Delete product
- `GET /api/admin/orders` - List all orders
- `GET /api/admin/orders/{id}` - Get order detail

## 🎨 Frontend Pages

- `/` - Home page
- `/products` - Product listing with filters
- `/products/[id]` - Product detail page
- `/cart` - Shopping cart
- `/checkout` - Checkout page
- `/orders` - Order history
- `/orders/[id]` - Order detail
- `/auth/login` - Login page
- `/auth/register` - Registration page
- `/admin` - Admin dashboard
- `/admin/products` - Product management
- `/admin/orders` - Order management

## 🔐 Authentication Flow

1. User registers or logs in
2. Backend generates JWT token
3. Frontend stores token in localStorage
4. Token is sent in Authorization header for protected routes
5. Backend validates token for each request

## 🗄️ Database Schema

### Users
- id, email, password_hash, full_name, phone, is_admin, is_active, created_at, updated_at

### Products
- id, name, description, price, category, sizes (JSON), colors (JSON), images (JSON), stock, is_active, popularity, created_at, updated_at

### Orders
- id, user_id, subtotal, tax, total_amount, status, shipping info, created_at, updated_at

### Order Items
- id, order_id, product_id, product_name, product_image, unit_price, quantity, selected_size, selected_color, created_at

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend (manual testing recommended)
1. Register a new user
2. Browse products and add to cart
3. Complete checkout process
4. View order history
5. Login as admin and manage products

## 🚀 Production Deployment

### Backend
1. Set secure `SECRET_KEY` in environment
2. Set `DEBUG=False`
3. Use production PostgreSQL database
4. Configure CORS properly
5. Use a production ASGI server (e.g., Gunicorn with Uvicorn workers)
6. Set up HTTPS

### Frontend
1. Build the production bundle: `npm run build`
2. Set production API URL
3. Deploy to Vercel, Netlify, or your preferred platform
4. Configure environment variables

## 📝 Environment Variables

### Backend (.env)
```env
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
FRONTEND_URL=http://localhost:3000
DEBUG=True
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - feel free to use this project for learning or commercial purposes.

## 💡 Tips

- Use the seeded test accounts to explore admin features
- Mock payment is implemented - orders are automatically marked as "PAID"
- Cart is stored in localStorage for anonymous users
- Admin features require logging in with an admin account

## 🐛 Troubleshooting

### Backend won't start
- Check PostgreSQL is running
- Verify DATABASE_URL is correct
- Ensure all dependencies are installed

### Frontend API errors
- Verify backend is running on port 8000
- Check NEXT_PUBLIC_API_URL in .env.local
- Ensure CORS is configured correctly in backend

### Database errors
- Run `python seed.py` to initialize database
- Check PostgreSQL user permissions
- Verify database exists

## 📧 Support

For issues or questions, please open an issue on GitHub.

---

**Happy Shopping! 🛍️**