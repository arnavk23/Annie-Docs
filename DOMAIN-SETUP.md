# 🌐 Setting Up annie.io Domain

This guide will help you make your documentation live at **annie.io** instead of just the local IP.

## 🎯 Quick Summary

To get annie.io live, you need to:
1. **Own the annie.io domain** (register it if you don't)
2. **Choose a hosting provider** (GitHub Pages, Netlify, etc.)
3. **Configure DNS** to point annie.io to your hosting provider
4. **Deploy your site**

---

## 📋 Step-by-Step Instructions

### Step 1: Domain Registration

**If you don't own annie.io yet:**

1. **Check availability**: Go to [Namecheap](https://namecheap.com), [GoDaddy](https://godaddy.com), or [Cloudflare](https://cloudflare.com)
2. **Search for "annie.io"**
3. **Purchase the domain** (usually $10-15/year)

**If you already own annie.io:**
- Log into your domain registrar's dashboard
- Find the DNS settings

---

### Step 2: Choose Hosting Method

## 🟢 **Option A: GitHub Pages (Free & Easy)**

### A1. Enable GitHub Pages

1. Go to your GitHub repository: `https://github.com/YOUR-USERNAME/Annie-Docs`
2. Click **Settings** → **Pages** (left sidebar)
3. Under **Source**, select **"GitHub Actions"**
4. The workflow is already configured (`.github/workflows/deploy-docs.yml`)

### A2. Configure Custom Domain

1. In GitHub Pages settings, under **Custom domain**
2. Enter: `annie.io`
3. Check **"Enforce HTTPS"**
4. GitHub will create a CNAME file automatically

### A3. Configure DNS at Your Domain Registrar

Add these DNS records at your domain registrar:

```
Type: A
Name: @
Value: 185.199.108.153

Type: A  
Name: @
Value: 185.199.109.153

Type: A
Name: @
Value: 185.199.110.153

Type: A
Name: @
Value: 185.199.111.153

Type: CNAME
Name: www
Value: YOUR-USERNAME.github.io
```

---

## 🟡 **Option B: Netlify (Easy with Features)**

### B1. Deploy to Netlify

1. Go to [netlify.com](https://netlify.com)
2. **"New site from Git"**
3. Connect your GitHub repository
4. Build settings (auto-detected from `netlify.toml`):
   - **Build command**: `pip install -r requirements.txt && mkdocs build`
   - **Publish directory**: `site`

### B2. Configure Custom Domain

1. In Netlify dashboard → **Domain settings**
2. **Add custom domain**: `annie.io`
3. Netlify will provide DNS instructions

### B3. Update DNS

At your domain registrar, add:

```
Type: A
Name: @
Value: 75.2.60.5

Type: CNAME
Name: www
Value: YOUR-SITE-NAME.netlify.app
```

---

## 🔵 **Option C: Vercel (Fast CDN)**

### C1. Deploy to Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy (from Annie-Docs directory)
vercel

# Follow prompts:
# - Project name: annie-docs
# - Deploy: Yes
```

### C2. Add Custom Domain

1. In Vercel dashboard → **Domains**
2. **Add**: `annie.io`
3. Follow DNS configuration instructions

---

## 🟠 **Option D: Cloudflare Pages (Fast & Free)**

### D1. Deploy to Cloudflare Pages

1. Go to [dash.cloudflare.com](https://dash.cloudflare.com) → **Pages**
2. **Create a project** → **Connect to Git**
3. Select your repository
4. Build settings:
   - **Build command**: `pip install -r requirements.txt && mkdocs build`
   - **Build output directory**: `site`

### D2. Custom Domain

1. **Custom domains** → **Set up a custom domain**
2. Enter: `annie.io`
3. Follow DNS instructions

---

## ⚡ **Quick Deploy Commands**

Since you've already committed your changes, you can now push to trigger deployment:

```bash
# Push to GitHub (triggers GitHub Actions)
git push origin main

# Check deployment status
# Go to: https://github.com/YOUR-USERNAME/Annie-Docs/actions
```

---

## 🔧 **DNS Configuration Examples**

### For GitHub Pages:
```dns
annie.io        A       185.199.108.153
annie.io        A       185.199.109.153  
annie.io        A       185.199.110.153
annie.io        A       185.199.111.153
www.annie.io    CNAME   YOUR-USERNAME.github.io
```

### For Netlify:
```dns
annie.io        A       75.2.60.5
www.annie.io    CNAME   YOUR-SITE.netlify.app
```

### For Cloudflare (if using Cloudflare DNS):
```dns
annie.io        A       (Cloudflare will auto-configure)
www.annie.io    CNAME   annie.io
```

---

## ⏱️ **Timeline**

- **Deployment**: 2-5 minutes (after push)
- **DNS Propagation**: 5 minutes - 48 hours
- **SSL Certificate**: Automatic (15-30 minutes)

---

## ✅ **Verification Steps**

1. **Check deployment**: Visit your hosting dashboard
2. **Test DNS**: Use [dns-lookup.com](https://dns-lookup.com) to check `annie.io`
3. **Verify SSL**: Ensure `https://annie.io` works
4. **Test site**: All pages and navigation work

---

## 🚀 **Next Steps**

### Immediate (Required):
1. **Push your code**: `git push origin main`
2. **Choose hosting provider** (recommend GitHub Pages)
3. **Configure DNS** at your domain registrar

### After DNS Propagates:
1. **Test annie.io** in browser
2. **Update any hardcoded URLs**
3. **Set up monitoring/analytics**

---

## 📞 **Need Help?**

**Common Issues:**
- **DNS not working**: Wait 24-48 hours for propagation
- **SSL errors**: Check with hosting provider
- **Build failures**: Check GitHub Actions logs

**Get Support:**
- GitHub Pages: [GitHub Support](https://support.github.com)
- Netlify: [Netlify Support](https://netlify.com/support)
- DNS Issues: Your domain registrar support

---

**🎯 Your goal**: Visit `https://annie.io` and see your documentation live!

Once DNS propagates, annie.io will show your professional documentation site instead of the local IP address.
