# 🌐 Hosting Guide

This guide covers multiple ways to make your Annie documentation site publicly accessible.

## 🚀 Quick Public Access (Local Network)

### Option 1: Network Access
Share your documentation with others on the same network:

```bash
./serve-public.sh
```

This makes your site accessible at:
- **Local**: `http://localhost:8000`
- **Network**: `http://YOUR-IP:8000` (shareable with others on your network)

### Option 2: Temporary Public URL
Create a temporary public URL using ngrok:

```bash
# Install ngrok first (see instructions in script)
./tunnel.sh
```

This creates a temporary public URL like `https://abc123.ngrok.io`

## 🏠 Free Hosting Services

### GitHub Pages (Recommended)

**Automatic deployment** - Push to trigger deployment:

1. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Source: "GitHub Actions"
   
2. **Push changes**:
   ```bash
   git add .
   git commit -m "docs: update documentation"
   git push origin main
   ```

3. **Access**: `https://YOUR-USERNAME.github.io/Annie-Docs/`

**✅ Pros**: Free, automatic builds, custom domains
**❌ Cons**: GitHub dependency, public repos only (free tier)

### Netlify

**One-click deployment**:

1. **Connect Repository**:
   - Go to [netlify.com](https://netlify.com)
   - "New site from Git" → Connect your GitHub repo
   
2. **Deploy Settings** (auto-detected via `netlify.toml`):
   - Build command: `pip install -r requirements.txt && mkdocs build`
   - Publish directory: `site`
   
3. **Custom Domain** (optional):
   - Add custom domain in Netlify dashboard
   - Annie-docs.netlify.app → your-domain.com

**✅ Pros**: Easy setup, instant deploys, branch previews, forms
**❌ Cons**: Build minutes limit (free tier)

### Vercel

**Deployment via CLI or Dashboard**:

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel
   ```
   
3. **Or via Dashboard**:
   - Import GitHub repo at [vercel.com](https://vercel.com)
   - Configuration auto-detected via `vercel.json`

**✅ Pros**: Fast edge network, great performance, preview deployments
**❌ Cons**: Node.js focused (but works with Python)

## 💻 Self-Hosting

### Simple HTTP Server

```bash
# Build site
mkdocs build

# Serve on custom port
cd site
python3 -m http.server 80  # Requires sudo for port 80

# Or with nginx
sudo apt install nginx
sudo cp -r site/* /var/www/html/
```

### Docker Container

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN mkdocs build

FROM nginx:alpine
COPY --from=0 /app/site /usr/share/nginx/html
EXPOSE 80
```

Build and run:
```bash
docker build -t annie-docs .
docker run -p 80:80 annie-docs
```

## ☁️ Cloud Hosting

### AWS S3 + CloudFront

```bash
# Build site
mkdocs build

# Upload to S3
aws s3 sync site/ s3://your-bucket-name --delete

# Configure S3 for static hosting
aws s3 website s3://your-bucket-name --index-document index.html
```

### Google Cloud Storage

```bash
# Build and upload
mkdocs build
gsutil -m cp -r site/* gs://your-bucket-name/

# Enable website configuration
gsutil web set -m index.html -e 404.html gs://your-bucket-name
```

## 🛡️ Security & Performance

### HTTPS Configuration

**Free SSL Certificates**:
- **Let's Encrypt**: Free SSL for custom domains
- **Cloudflare**: Free tier includes SSL
- **GitHub Pages**: Automatic HTTPS
- **Netlify/Vercel**: Free SSL included

### Performance Optimization

**Content Delivery Network (CDN)**:
- **Cloudflare**: Free tier available
- **AWS CloudFront**: Pay-per-use
- **Netlify/Vercel**: CDN included

**Optimization tips**:
```bash
# Minify during build (add to mkdocs.yml)
plugins:
  - minify:
      minify_html: true
      minify_css: true
      minify_js: true
```

## 📊 Monitoring & Analytics

### Google Analytics

Add to `mkdocs.yml`:
```yaml
google_analytics:
  - 'UA-XXXXXXXX-X'
  - 'auto'
```

### Simple Analytics

```html
<!-- Add to custom theme -->
<script async defer src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
```

## 🔧 Continuous Deployment

### GitHub Actions (Included)

The `.github/workflows/deploy-docs.yml` automatically:
1. Builds documentation on every push
2. Deploys to GitHub Pages
3. Updates live site within minutes

### Webhook Deployment

For custom servers, create a webhook endpoint:
```bash
# webhook.php
<?php
if ($_POST['secret'] === 'your-secret') {
    exec('cd /path/to/docs && git pull && mkdocs build');
}
?>
```

## 📱 Mobile Optimization

The ReadTheDocs theme is mobile-responsive, but test on:
- 📱 Mobile phones (320px+)
- 📱 Tablets (768px+)
- 💻 Desktop (1024px+)

## 🔍 SEO Optimization

Add to `mkdocs.yml`:
```yaml
site_name: Annie Documentation
site_description: Blazingly fast Approximate Nearest Neighbors in Rust
site_url: https://your-domain.com

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/Programmers-Paradise/Annie
    - icon: fontawesome/brands/python
      link: https://pypi.org/project/rust-annie/
```

## ❓ Troubleshooting

### Common Issues

**Build Fails**:
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
rm -rf venv
./build-docs.sh
```

**404 Errors**:
- Check `mkdocs.yml` navigation paths
- Verify file names match exactly
- Ensure case sensitivity

**Slow Loading**:
- Enable gzip compression
- Use CDN
- Optimize images
- Minify CSS/JS

### Getting Help

- 🐛 [Report issues](https://github.com/Programmers-Paradise/Annie-Docs/issues)
- 💬 [Ask questions](https://github.com/Programmers-Paradise/Annie-Docs/discussions)
- 📧 Contact maintainers

---

**Choose the hosting option that best fits your needs:**
- 🏠 **Local/Testing**: `./serve-public.sh`
- 🌐 **Temporary Public**: `./tunnel.sh`
- 🆓 **Free Hosting**: GitHub Pages, Netlify, Vercel
- 💼 **Professional**: AWS, Google Cloud, self-hosted
