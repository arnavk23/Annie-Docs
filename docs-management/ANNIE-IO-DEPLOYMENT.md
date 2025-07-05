# 🌐 Deploy to annie.io - Complete Guide

This guide provides step-by-step instructions to make your documentation live at https://annie.io.

## 📋 Prerequisites

Before starting, ensure you have:

- ✅ **Domain ownership**: You must own the `annie.io` domain
- ✅ **DNS access**: Ability to modify DNS records at your domain registrar
- ✅ **GitHub repository**: This documentation repository is public or you have GitHub Pro
- ✅ **Content ready**: Documentation is built and tested locally

## 🚀 Deployment Options

### Option 1: GitHub Pages (Recommended - Free)

#### Step 1: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **GitHub Actions**
5. Under **Custom domain**, enter: `annie.io`
6. Check **Enforce HTTPS** ✅

#### Step 2: Configure DNS Records

At your domain registrar (GoDaddy, Namecheap, Cloudflare, etc.), add these DNS records:

```dns
Type: A     Name: @      Value: 185.199.108.153
Type: A     Name: @      Value: 185.199.109.153
Type: A     Name: @      Value: 185.199.110.153
Type: A     Name: @      Value: 185.199.111.153
Type: CNAME Name: www    Value: programmers-paradise.github.io
```

#### Step 3: Deploy

```bash
# Commit and push your latest changes
git add .
git commit -m "docs: final updates for annie.io deployment"
git push origin main
```

The deployment workflow will automatically run and deploy to GitHub Pages.

#### Step 4: Wait for DNS Propagation

- **DNS propagation**: 5 minutes to 48 hours (usually within 1 hour)
- **SSL certificate**: Automatic (GitHub handles this)
- **Verification**: Visit `https://annie.io` to check

### Option 2: Netlify (Easy Setup)

#### Step 1: Connect Repository

1. Go to [netlify.com](https://netlify.com) and sign in
2. Click **New site from Git**
3. Choose **GitHub** and select this repository
4. Build settings are automatically detected from `netlify.toml`

#### Step 2: Configure Domain

1. In Netlify dashboard, go to **Domain settings**
2. Click **Add custom domain**
3. Enter: `annie.io`
4. Follow Netlify's DNS instructions

#### Step 3: Update DNS

At your domain registrar, add these records:

```dns
Type: CNAME Name: @      Value: YOUR-SITE-NAME.netlify.app
Type: CNAME Name: www    Value: YOUR-SITE-NAME.netlify.app
```

### Option 3: Vercel (High Performance)

#### Step 1: Connect Repository

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click **New Project**
3. Import from GitHub and select this repository
4. Settings are automatically detected from `vercel.json`

#### Step 2: Configure Domain

1. In Vercel dashboard, go to **Domains**
2. Add domain: `annie.io`
3. Follow Vercel's DNS instructions

## 🔧 Configuration Files

The repository includes pre-configured files for each platform:

### GitHub Pages

- `.github/workflows/deploy-docs.yml` - Automated deployment
- `configs/CNAME` - Custom domain configuration

### Netlify

- `configs/netlify.toml` - Build and deployment settings

### Vercel

- `configs/vercel.json` - Build and routing configuration

## 🛠️ Build Process

The documentation is built using MkDocs with these steps:

```bash
# Install dependencies
pip install -r requirements.txt

# Build static site
mkdocs build

# Output goes to site/ directory
```

## 🔍 Verification Steps

After deployment, verify these elements:

### ✅ Basic Functionality

- [ ] Site loads at `https://annie.io`
- [ ] All pages are accessible
- [ ] Navigation works correctly
- [ ] Search functionality works

### ✅ Performance

- [ ] Page load times < 3 seconds
- [ ] Images load properly
- [ ] Mobile responsiveness

### ✅ SEO & Analytics

- [ ] Proper meta tags
- [ ] Sitemap accessible at `/sitemap.xml`
- [ ] SSL certificate is valid

## 🚨 Troubleshooting

### Domain Not Working

**DNS Issues:**

```bash
# Check DNS propagation
nslookup annie.io
dig annie.io

# Check specific DNS servers
nslookup annie.io 8.8.8.8
```

**GitHub Pages Issues:**

- Verify custom domain is set in repository settings
- Check that CNAME file exists in configs/
- Ensure repository is public or you have GitHub Pro

### SSL Certificate Issues

**GitHub Pages:**

- SSL certificates are automatic but can take up to 24 hours
- Check repository settings → Pages → Enforce HTTPS

**Netlify/Vercel:**

- Both provide automatic SSL certificates
- Check domain settings in respective dashboards

### Build Failures

**Check workflow logs:**

1. Go to Actions tab in GitHub
2. Click on failed workflow run
3. Expand logs to see specific errors

**Common issues:**

- Missing dependencies in `requirements.txt`
- Invalid MkDocs configuration
- Missing markdown files

## 📊 Monitoring & Maintenance

### Automated Updates

- Documentation syncs automatically from main Annie repository
- Deployments happen on every push to main branch
- Status visible in GitHub Actions tab

### Manual Monitoring

- **Uptime**: Use services like UptimeRobot
- **Performance**: Google PageSpeed Insights
- **Analytics**: Google Analytics or similar

### Regular Maintenance

- Update dependencies in `requirements.txt`
- Review and update documentation content
- Monitor for broken links

## 🎉 Go Live Checklist

Before announcing annie.io publicly:

- [ ] All DNS records configured correctly
- [ ] SSL certificate is active and valid
- [ ] All documentation pages load correctly
- [ ] Search functionality works
- [ ] Auto-sync from main repository is working
- [ ] Contact/support information is up to date
- [ ] Analytics/monitoring is set up
- [ ] 404 page is properly configured
- [ ] Sitemap is accessible and current

## 🆘 Support

If you encounter issues:

1. **Check workflow logs** in the Actions tab
2. **Review DNS settings** at your domain registrar
3. **Test locally** with `mkdocs serve`
4. **Create an issue** in this repository with details

---

_Once deployed, annie.io will be your professional documentation home! 🏠_
