#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${RED}🛑 Stopping Development Servers${NC}"
echo "================================"
echo ""

# Check if PID file exists
if [ -f ".dev-pids" ]; then
    # Read PIDs
    BACKEND_PID=$(sed -n '1p' .dev-pids)
    FRONTEND_PID=$(sed -n '2p' .dev-pids)
    
    # Stop backend
    if ps -p $BACKEND_PID > /dev/null 2>&1; then
        echo "Stopping backend (PID: $BACKEND_PID)..."
        kill $BACKEND_PID
        echo -e "${GREEN}✅ Backend stopped${NC}"
    else
        echo "⚠️  Backend process not found"
    fi
    
    # Stop frontend
    if ps -p $FRONTEND_PID > /dev/null 2>&1; then
        echo "Stopping frontend (PID: $FRONTEND_PID)..."
        kill $FRONTEND_PID
        echo -e "${GREEN}✅ Frontend stopped${NC}"
    else
        echo "⚠️  Frontend process not found"
    fi
    
    # Clean up PID file
    rm .dev-pids
    echo ""
    echo -e "${GREEN}All servers stopped!${NC}"
else
    echo "⚠️  No running servers found (.dev-pids not found)"
    echo ""
    echo "Trying to kill by port..."
    
    # Try to find and kill processes on ports 8000 and 3000
    BACKEND_PID=$(lsof -ti:8000)
    FRONTEND_PID=$(lsof -ti:3000)
    
    if [ ! -z "$BACKEND_PID" ]; then
        echo "Killing process on port 8000 (PID: $BACKEND_PID)"
        kill $BACKEND_PID
    fi
    
    if [ ! -z "$FRONTEND_PID" ]; then
        echo "Killing process on port 3000 (PID: $FRONTEND_PID)"
        kill $FRONTEND_PID
    fi
    
    if [ -z "$BACKEND_PID" ] && [ -z "$FRONTEND_PID" ]; then
        echo "No processes found on ports 8000 or 3000"
    fi
fi