#!/bin/bash

# Annie Documentation Public Server
# Makes the documentation site publicly accessible

echo "🌐 Annie.io Documentation - Public Server"
echo "========================================"

# Check if site is built
if [ ! -d "site" ]; then
    echo "📁 Site directory not found. Building documentation..."
    ./build-docs.sh
    if [ $? -ne 0 ]; then
        echo "❌ Build failed. Please fix the issues and try again."
        exit 1
    fi
fi

echo "🔧 Starting public server..."

# Get local IP address
LOCAL_IP=$(hostname -I | awk '{print $1}')
PORT=8080

echo "📡 Server will be accessible at:"
echo "   🏠 Local:    http://localhost:$PORT"
echo "   🌍 Network:  http://$LOCAL_IP:$PORT"
echo ""
echo "💡 Share the Network URL with others on your network!"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

# Start server accessible from all interfaces
cd site
python3 -m http.server $PORT --bind 0.0.0.0
