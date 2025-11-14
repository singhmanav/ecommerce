#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🛍️  E-Commerce App - Development Server${NC}"
echo "========================================"
echo ""

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo -e "${YELLOW}Checking prerequisites...${NC}"

if ! command_exists python3; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

if ! command_exists node; then
    echo "❌ Node.js is required but not installed."
    exit 1
fi

if ! command_exists psql; then
    echo "⚠️  PostgreSQL CLI not found. Ensure PostgreSQL is running."
fi

echo -e "${GREEN}✅ Prerequisites OK${NC}"
echo ""

# Function to check if port is in use
check_port() {
    lsof -i:$1 >/dev/null 2>&1
}

# Check if servers are already running
if check_port 8000; then
    echo "⚠️  Port 8000 is already in use. Backend might already be running."
    echo "   Stop it first or use a different port."
    exit 1
fi

if check_port 3000; then
    echo "⚠️  Port 3000 is already in use. Frontend might already be running."
    echo "   Stop it first or use a different port."
    exit 1
fi

# Start backend
echo -e "${BLUE}🚀 Starting Backend Server...${NC}"
cd backend

# Activate virtual environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Run ./setup.sh first."
    exit 1
fi

# Start backend in background
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 > ../backend.log 2>&1 &
BACKEND_PID=$!
echo -e "${GREEN}✅ Backend started (PID: $BACKEND_PID)${NC}"
echo "   Logs: backend.log"
echo "   API: http://localhost:8000"
echo "   Docs: http://localhost:8000/docs"

cd ..

# Wait for backend to be ready
echo -e "${YELLOW}⏳ Waiting for backend to be ready...${NC}"
sleep 3

# Start frontend
echo ""
echo -e "${BLUE}🚀 Starting Frontend Server...${NC}"
cd frontend

npm run dev > ../frontend.log 2>&1 &
FRONTEND_PID=$!
echo -e "${GREEN}✅ Frontend started (PID: $FRONTEND_PID)${NC}"
echo "   Logs: frontend.log"
echo "   App: http://localhost:3000"

cd ..

# Save PIDs to file for cleanup
echo "$BACKEND_PID" > .dev-pids
echo "$FRONTEND_PID" >> .dev-pids

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}🎉 Development servers are running!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "📱 Frontend:  http://localhost:3000"
echo "🔧 Backend:   http://localhost:8000"
echo "📚 API Docs:  http://localhost:8000/docs"
echo ""
echo -e "${YELLOW}Test Accounts:${NC}"
echo "  Admin: admin@example.com / admin123"
echo "  User:  user@example.com / user123"
echo ""
echo -e "${YELLOW}To stop the servers:${NC}"
echo "  Run: ./stop.sh"
echo "  Or:  kill $BACKEND_PID $FRONTEND_PID"
echo ""
echo "Press Ctrl+C to see logs (servers will keep running)"
echo ""

# Tail logs
tail -f backend.log frontend.log