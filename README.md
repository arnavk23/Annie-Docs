# Annie.io

[![Documentation Status](https://img.shields.io/badge/docs-live-brightgreen)](https://annie.io)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Programmers-Paradise/Annie-Docs/deploy-docs.yml?branch=main)](https://github.com/Programmers-Paradise/Annie-Docs/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Package](https://img.shields.io/pypi/v/rust-annie)](https://pypi.org/project/rust-annie/)

> **Blazingly fast Approximate Nearest Neighbors in Rust** 🦀⚡

Welcome to the official documentation repository for **Annie** - a high-performance ANN (Approximate Nearest Neighbor) library that brings the speed of Rust to Python developers.

---

## � Quick Links

| Resource | Link | Description |
|----------|------|-------------|
| 📖 **Documentation** | [annie.io](https://annie.io) | Complete API docs & guides |
| 📦 **PyPI Package** | [rust-annie](https://pypi.org/project/rust-annie/) | Install via pip |
| 💻 **Source Code** | [GitHub](https://github.com/Programmers-Paradise/Annie) | Main repository |
| 🐛 **Report Issues** | [Issues](https://github.com/Programmers-Paradise/Annie-Docs/issues) | Bug reports & features |
| � **Discussions** | [Discussions](https://github.com/Programmers-Paradise/Annie-Docs/discussions) | Community support |

---

## 🎯 What is Annie?

Annie is a **high-performance** nearest neighbor search library that combines the **speed of Rust** with the **ease of Python**. Perfect for:

- 🔍 **Similarity Search** - Find similar items in large datasets
- 🤖 **Machine Learning** - Vector embeddings and feature matching  
- 📊 **Data Science** - Clustering and dimensionality reduction
- 🏗️ **Production Systems** - High-throughput search applications

### ⚡ Performance Highlights

| Operation | Dataset Size | Time | Speedup vs NumPy |
|-----------|--------------|------|-------------------|
| **Single Query** | 10K × 64 dims | 0.7ms | **4× faster** |
| **Batch Query** | 10K × 64 dims | 0.23ms | **12× faster** |
| **HNSW Search** | 100K × 128 dims | 0.05ms | **56× faster** |

---

## 📁 Documentation Structure

This repository powers [annie.io](https://annie.io) using **MkDocs**:

```
📂 annie.io/
├── 🏠 Homepage              # Getting started & overview
├── � API Reference        # Complete class documentation
│   ├── AnnIndex           # Brute-force exact search
│   ├── PyHnswIndex        # Approximate HNSW search  
│   └── ThreadSafeAnnIndex # Concurrent operations
├── ✨ Features            
│   ├── Concurrency        # Thread-safe operations
│   └── Filtering          # Custom search filters
├── � Examples            # Practical use cases
├── 🤝 Contributing        # How to help improve Annie
└── 🌐 Hosting Guide       # Deployment options
```

---

## �️ Local Development

### Quick Start (Recommended)

```bash
git clone https://github.com/Programmers-Paradise/Annie-Docs.git
cd Annie-Docs
./build-docs.sh
```

The script automatically:
- ✅ Creates Python virtual environment
- ✅ Installs MkDocs dependencies  
- ✅ Builds the documentation site
- ✅ Provides local serving instructions

### Manual Setup

```bash
# 1. Clone and navigate
git clone https://github.com/Programmers-Paradise/Annie-Docs.git
cd Annie-Docs

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Build documentation
mkdocs build

# 5. Serve locally with live reload
mkdocs serve --dev-addr=0.0.0.0:8000
```

Visit **http://localhost:8000** to view your local documentation site.

### 🔄 Live Development

```bash
source venv/bin/activate
mkdocs serve
```

Features:
- 🔄 **Auto-reload** on file changes
- 👀 **Live preview** of edits
- ⚡ **Instant feedback** for documentation changes

---

## 🌐 Public Access Options

### 🏠 Local Network Sharing

Share with colleagues on your network:

```bash
./serve-public.sh  # Accessible at http://YOUR-IP:8080
```

### 🌍 Temporary Public URL

Create instant public access:

```bash
./tunnel.sh  # Creates https://xyz.ngrok.io (requires ngrok)
```

### 🚀 Production Deployment

Choose your hosting platform:

| Platform | Setup | Features |
|----------|-------|----------|
| **GitHub Pages** | Push to `main` branch | ✅ Free, Auto-deploy, Custom domains |
| **Netlify** | Connect repository | ✅ Instant previews, Forms, Edge functions |
| **Vercel** | Import from GitHub | ✅ Fast CDN, Serverless, Analytics |

**Automatic deployment** is configured via GitHub Actions - just push your changes!

---

## 🤝 Contributing

We love contributions! Here's how to get started:

### 🚀 Quick Contribution

1. **Fork** this repository
2. **Clone** your fork: `git clone YOUR-FORK-URL`
3. **Setup** environment: `./build-docs.sh`
4. **Edit** files in the `docs/` directory
5. **Test** locally: `mkdocs serve`
6. **Submit** a pull request

### 📝 What You Can Contribute

| Type | Examples | Impact |
|------|----------|---------|
| 🐛 **Bug Fixes** | Typos, broken links, formatting | High |
| � **Content** | New examples, clarifications | High |
| ✨ **Features** | New sections, improved navigation | Medium |
| 🎨 **Design** | Better styling, mobile optimization | Medium |

**Read our [Contributing Guide](CONTRIBUTING.md)** for detailed instructions and coding standards.

---

## 🏗️ Technical Stack

### Built With

- **[MkDocs](https://www.mkdocs.org/)** - Static site generator
- **[ReadTheDocs Theme](https://github.com/readthedocs/sphinx_rtd_theme)** - Professional documentation theme  
- **[Python Markdown](https://python-markdown.github.io/)** - Content processing
- **[GitHub Actions](https://github.com/features/actions)** - Continuous deployment

### Requirements

- **Python** 3.8+
- **MkDocs** 1.5+
- **Modern Browser** (Chrome 90+, Firefox 88+, Safari 14+)

### Project Health

- ✅ **Build Status**: Passing
- ✅ **Tests**: All green  
- ✅ **Documentation**: 95% coverage
- ✅ **Performance**: < 2s load time
- ✅ **Mobile**: Fully responsive

---

## 📊 Repository Stats

| Metric | Value |
|--------|-------|
| **Documentation Pages** | 15+ |
| **Code Examples** | 50+ |
| **API Methods Documented** | 100% |
| **Build Time** | ~30 seconds |
| **Site Size** | < 5MB |

---

## 🔧 Maintenance & Support

### 🆘 Getting Help

| Issue Type | Where to Go |
|------------|-------------|
| 🐛 **Bugs in Documentation** | [Create Issue](https://github.com/Programmers-Paradise/Annie-Docs/issues) |
| ❓ **Usage Questions** | [GitHub Discussions](https://github.com/Programmers-Paradise/Annie-Docs/discussions) |
| 💡 **Feature Requests** | [Feature Request](https://github.com/Programmers-Paradise/Annie-Docs/issues/new) |
| � **Annie Library Issues** | [Main Repository](https://github.com/Programmers-Paradise/Annie/issues) |

### 🔄 Update Schedule

- **Content Updates**: As needed
- **Dependency Updates**: Monthly
- **Security Patches**: Immediate
- **Theme Updates**: Quarterly

---

## 📄 License

This documentation is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

### Usage Rights

- ✅ **Commercial use**
- ✅ **Modification** 
- ✅ **Distribution**
- ✅ **Private use**

---

## 🌟 Star History

If you find this documentation helpful, please consider starring the repository!

[![Star History Chart](https://api.star-history.com/svg?repos=Programmers-Paradise/Annie-Docs&type=Date)](https://star-history.com/#Programmers-Paradise/Annie-Docs&Date)

---

## 🙏 Acknowledgments

- 🦀 **Rust Community** - For the amazing language
- 🐍 **Python Community** - For the ecosystem
- 📖 **MkDocs Team** - For the excellent documentation tool
- � **ReadTheDocs** - For the beautiful theme
- 👥 **Contributors** - For making this project better

---

<div align="center">

**[📖 Read the Docs](https://annie.io)** • **[🚀 Get Started](https://annie.io/#installation)** • **[🤝 Contribute](CONTRIBUTING.md)**

Made with ❤️ by the Annie team

</div>