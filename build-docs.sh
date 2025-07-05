# Annie Documentation Build Script

echo "Annie.io Documentation Builder"
echo "=============================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies if not already installed
echo "Installing dependencies..."
pip install mkdocs >/dev/null 2>&1

# Build documentation
echo "Building documentation..."
mkdocs build

if [ $? -eq 0 ]; then
    echo "✓ Documentation built successfully!"
    echo "✓ Site is available in the 'site/' directory"
    echo ""
    echo "To serve locally, run:"
    echo "  source venv/bin/activate && mkdocs serve"
else
    echo "✗ Build failed!"
    exit 1
fi
