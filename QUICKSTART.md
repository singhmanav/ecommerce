# 🚀 Quick Start Guide

Get your e-commerce app running in 5 minutes!

## Option 1: Automated Setup (Recommended)

### Run the setup script:

```bash
./setup.sh
```

This will:
- Check prerequisites
- Set up Python virtual environment
- Install all dependencies
- Create environment files

### Create and seed the database:

```bash
# Create database
createdb ecommerce_db

# Seed with sample data
cd backend
source venv/bin/activate
python seed.py
```

### Start the servers:

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

**Access the app:** http://localhost:3000

---

## Option 2: Docker (Easiest)

### Start everything with Docker:

```bash
docker-compose up -d
```

### Seed the database:

```bash
docker-compose exec backend python seed.py
```

**Access the app:** http://localhost:3000

---

## Test Accounts

After seeding the database, use these accounts:

**Admin Account:**
- Email: `admin@example.com`
- Password: `admin123`

**Regular User Account:**
- Email: `user@example.com`
- Password: `user123`

---

## What You Can Do

### As a User:
1. Browse products with filters
2. View product details
3. Add items to cart
4. Complete checkout
5. View order history

### As an Admin:
1. Login with admin account
2. Go to `/admin`
3. Manage products (create, edit, delete)
4. View all orders

---

## API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Troubleshooting

### Backend won't start?
- Ensure PostgreSQL is running
- Check `backend/.env` has correct DATABASE_URL
- Try: `cd backend && source venv/bin/activate && pip install -r requirements.txt`

### Frontend errors?
- Check `frontend/.env.local` has correct API URL
- Try: `cd frontend && rm -rf .next && npm run dev`

### Database errors?
- Run: `createdb ecommerce_db`
- Then: `python seed.py`

---

## Project Structure

```
ecomerce-app/
├── backend/              # FastAPI (Python)
│   ├── app/
│   │   ├── api/         # Routes
│   │   ├── models/      # Database models
│   │   ├── schemas/     # Pydantic schemas
│   │   └── core/        # Config & security
│   └── seed.py          # Database seeder
│
├── frontend/             # Next.js (TypeScript)
│   ├── app/             # Pages (App Router)
│   ├── components/      # React components
│   ├── lib/             # API & utilities
│   └── types/           # TypeScript types
│
├── docker-compose.yml    # Docker configuration
├── setup.sh             # Setup script
└── README.md            # Full documentation
```

---

## Next Steps

1. ✅ Get the app running
2. 📚 Read the full [README.md](README.md) for detailed docs
3. 🎨 Customize the design
4. 🚀 Deploy to production
5. ⭐ Star the repo if you find it useful!

---

**Need help?** Open an issue on GitHub or check the full README.md