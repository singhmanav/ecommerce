# 🚀 Deployment Guide - Render.com

This guide will help you deploy your e-commerce application to Render.com.

## Prerequisites

1. GitHub account
2. Render.com account (free tier works!)
3. Your code pushed to GitHub

---

## Part 1: Push to GitHub

### 1. Create a new repository on GitHub

Go to https://github.com/new and create a repository named `ecommerce-clothing-store`

### 2. Push your code

```bash
cd "/Users/manav/Desktop/ecomerce app"

# Add all files
git add .

# Commit
git commit -m "Initial commit: Full-stack e-commerce app"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/ecommerce-clothing-store.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Part 2: Deploy Backend on Render

### 1. Create PostgreSQL Database

1. Go to https://dashboard.render.com/
2. Click **"New +"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `ecommerce-db`
   - **Database**: `ecommerce_db`
   - **User**: `ecommerce_user`
   - **Region**: Choose closest to you
   - **Plan**: Free
4. Click **"Create Database"**
5. **Save the Internal Database URL** - you'll need it!

### 2. Deploy Backend Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure:
   - **Name**: `ecommerce-backend`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

4. **Environment Variables** (click "Advanced"):
   ```
   DATABASE_URL = [paste your Internal Database URL from step 1]
   SECRET_KEY = [generate a random string - use a password generator]
   ALGORITHM = HS256
   ACCESS_TOKEN_EXPIRE_MINUTES = 30
   DEBUG = False
   FRONTEND_URL = https://your-frontend-url.vercel.app
   ```

5. Click **"Create Web Service"**

6. Wait for deployment (5-10 minutes)

7. **Copy your backend URL**: `https://ecommerce-backend-xxxx.onrender.com`

### 3. Seed the Database

Once deployed, use Render's Shell:

1. Go to your backend service dashboard
2. Click **"Shell"** in the top navigation
3. Run:
   ```bash
   python seed.py
   ```

---

## Part 3: Deploy Frontend on Vercel (Recommended)

Vercel is better for Next.js apps:

### 1. Deploy to Vercel

1. Go to https://vercel.com
2. Click **"Import Project"**
3. Connect your GitHub repository
4. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

5. **Environment Variables**:
   ```
   NEXT_PUBLIC_API_URL = https://your-backend-url.onrender.com/api
   ```
   Replace with your actual Render backend URL from Part 2, step 7

6. Click **"Deploy"**

7. Your frontend will be live at: `https://your-app.vercel.app`

### 2. Update Backend CORS

Go back to Render backend settings and update:
```
FRONTEND_URL = https://your-app.vercel.app
```

Click **"Save Changes"** - backend will redeploy.

---

## Alternative: Deploy Frontend on Render

If you prefer everything on Render:

1. Click **"New +"** → **"Static Site"**
2. Connect your GitHub repository
3. Configure:
   - **Name**: `ecommerce-frontend`
   - **Branch**: `main`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `.next`

4. **Environment Variables**:
   ```
   NEXT_PUBLIC_API_URL = https://your-backend-url.onrender.com/api
   ```

---

## Part 4: Test Your Deployment

### 1. Test Backend

Visit: `https://your-backend-url.onrender.com/docs`

You should see the Swagger API documentation.

### 2. Test Frontend

Visit: `https://your-app.vercel.app`

Try:
1. Register a new account
2. Browse products
3. Add items to cart
4. Complete checkout

### 3. Test Admin

Login with:
- Email: `admin@example.com`
- Password: `admin123`

Go to `/admin` and test product management.

---

## 🔧 Troubleshooting

### Backend Issues

**Error: Database connection failed**
- Check DATABASE_URL is correct
- Ensure database and backend are in same region
- Check database is active

**Error: CORS issues**
- Verify FRONTEND_URL in backend environment variables
- Make sure it matches your actual frontend URL
- No trailing slash in URL

**Error: Module not found**
- Check build command ran successfully
- Verify requirements.txt is in backend folder
- Check build logs in Render dashboard

### Frontend Issues

**Error: API calls failing**
- Verify NEXT_PUBLIC_API_URL is correct
- Must include `/api` at the end
- Check backend is deployed and running

**Error: Build failed**
- Check Node.js version (18+ required)
- Verify package.json is correct
- Check build logs in Vercel/Render

### Database Not Seeded

SSH into Render backend:
```bash
python seed.py
```

---

## 📊 Monitoring

### Render Dashboard
- Monitor backend health
- View logs
- Check database usage

### Vercel Dashboard
- Monitor frontend performance
- View deployment logs
- Check analytics

---

## 💰 Pricing

### Free Tier Limits

**Render (Backend + Database)**
- 750 hours/month (enough for 1 app)
- Database: 90 days retention, then deleted
- Backend: Spins down after 15 min inactivity
- **Note**: First request after sleep takes 30-60s

**Vercel (Frontend)**
- Unlimited bandwidth
- 100 GB-hours/month
- Perfect for frontend hosting

### Upgrade If Needed

If your app grows:
- Render: $7/month (backend) + $7/month (database)
- Vercel: Free is usually enough for frontend

---

## 🎯 Production Checklist

Before going live:

- [ ] Change SECRET_KEY to a strong random string
- [ ] Set DEBUG=False
- [ ] Update FRONTEND_URL to production URL
- [ ] Set up custom domain (optional)
- [ ] Test all features work in production
- [ ] Set up monitoring/alerts
- [ ] Back up database regularly
- [ ] Update README with production URLs

---

## 🔐 Security Notes

1. **Never commit .env files**
2. **Use strong SECRET_KEY**
3. **Keep dependencies updated**
4. **Monitor for suspicious activity**
5. **Set up database backups**

---

## 📱 Custom Domain (Optional)

### For Vercel (Frontend)
1. Go to project settings
2. Click "Domains"
3. Add your custom domain
4. Update DNS records as instructed

### For Render (Backend)
1. Go to service settings
2. Click "Custom Domains"
3. Add your custom domain
4. Update DNS records as instructed

---

## 🆘 Need Help?

1. **Render Issues**: https://render.com/docs
2. **Vercel Issues**: https://vercel.com/docs
3. **App Issues**: Check GitHub issues
4. **Community**: Join Render/Vercel Discord

---

## 🎉 Congratulations!

Your e-commerce app is now live on the internet!

Share your URLs:
- Frontend: `https://your-app.vercel.app`
- Backend API: `https://your-backend.onrender.com`
- API Docs: `https://your-backend.onrender.com/docs`

**Next steps:**
1. Share with friends
2. Add more features
3. Customize the design
4. Scale as needed

---

## Quick Reference

```bash
# Backend URL format
https://ecommerce-backend-xxxx.onrender.com

# Frontend URL format
https://your-app.vercel.app

# API endpoint format
https://ecommerce-backend-xxxx.onrender.com/api/products

# Environment variables needed
Backend:
  - DATABASE_URL (from Render PostgreSQL)
  - SECRET_KEY (generate random string)
  - ALGORITHM = HS256
  - FRONTEND_URL (your Vercel URL)
  
Frontend:
  - NEXT_PUBLIC_API_URL (your Render backend URL + /api)
```

Happy deploying! 🚀