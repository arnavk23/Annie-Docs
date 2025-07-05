#!/bin/bash

# Annie Documentation Tunnel Service
# Creates a public URL for your documentation using ngrok

echo "🌐 Annie.io Documentation Tunnel Service"
echo "========================================"

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok is not installed."
    echo ""
    echo "📦 Install ngrok:"
    echo "   1. Download from: https://ngrok.com/download"
    echo "   2. Or install via package manager:"
    echo "      - Ubuntu/Debian: snap install ngrok"
    echo "      - macOS: brew install ngrok"
    echo "      - Windows: choco install ngrok"
    echo ""
    echo "🔑 Then sign up and authenticate:"
    echo "   ngrok config add-authtoken YOUR_TOKEN"
    exit 1
fi

# Check if site is built
if [ ! -d "site" ]; then
    echo "📁 Site directory not found. Building documentation..."
    ./build-docs.sh
    if [ $? -ne 0 ]; then
        echo "❌ Build failed. Please fix the issues and try again."
        exit 1
    fi
fi

PORT=8000

echo "🚀 Starting local server..."

# Start local server in background
cd site
python3 -m http.server $PORT --bind 127.0.0.1 &
SERVER_PID=$!

# Wait a moment for server to start
sleep 2

echo "🔗 Creating public tunnel..."

# Start ngrok tunnel
ngrok http $PORT --log=stdout &
NGROK_PID=$!

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    kill $SERVER_PID $NGROK_PID 2>/dev/null
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

echo ""
echo "✅ Services started!"
echo "📝 Your documentation is now publicly accessible"
echo "🌍 Check the ngrok output above for your public URL"
echo "🛑 Press Ctrl+C to stop all services"
echo ""

# Wait for processes
wait
