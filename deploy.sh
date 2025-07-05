#!/bin/bash

# Annie Documentation Deployment Script

echo "Annie.io Documentation Deployment"
echo "================================="

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✓ Virtual environment activated"
else
    echo "✗ Virtual environment not found. Run ./build-docs.sh first."
    exit 1
fi

# Clean and build
echo "Building documentation..."
mkdocs build --clean

if [ $? -eq 0 ]; then
    echo "✓ Documentation built successfully!"
    
    # Copy any additional assets if needed
    if [ -f "assets/favicon.ico" ]; then
        cp assets/favicon.ico site/
        echo "✓ Assets copied"
    fi
    
    echo ""
    echo "✓ Site is ready for deployment in 'site/' directory"
    echo "  You can now deploy the contents of the 'site/' folder"
    echo "  to your web server or hosting platform."
else
    echo "✗ Build failed!"
    exit 1
fi
