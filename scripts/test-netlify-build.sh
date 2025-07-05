#!/bin/bash
# Netlify deployment test script
set -e

echo "🧪 Testing Netlify Deployment Process..."

# Create test environment
python3 -m venv netlify_test_env
source netlify_test_env/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# Build site
echo "🏗️ Building documentation..."
mkdocs build --verbose

# Copy redirects
echo "📋 Copying _redirects file..."
cp docs/_redirects site/_redirects

# Verify build
echo "✅ Verifying build..."
if [ -f "site/index.html" ]; then
    echo "✓ index.html exists"
else
    echo "✗ index.html missing"
    exit 1
fi

if [ -f "site/_redirects" ]; then
    echo "✓ _redirects file exists"
else
    echo "✗ _redirects file missing"
    exit 1
fi

# Check for content
if grep -q "Annie.io" site/index.html; then
    echo "✓ Content found in index.html"
else
    echo "✗ Content missing from index.html"
    exit 1
fi

echo "🎉 Build test completed successfully!"
echo "📁 Built site is in: ./site/"

# Cleanup
deactivate
rm -rf netlify_test_env

echo "💡 If Netlify is still showing errors, check:"
echo "   1. Build logs in Netlify dashboard"
echo "   2. Ensure netlify.toml is in repository root"
echo "   3. Check Python version in Netlify settings"
echo "   4. Verify all files are committed to git"
