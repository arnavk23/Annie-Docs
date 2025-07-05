# Annie.io Documentation

[![Documentation](https://img.shields.io/badge/docs-netlify-blue)](https://annie-docs.netlify.app/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Programmers-Paradise/Annie-Docs/deploy-docs.yml?branch=main)](https://github.com/Programmers-Paradise/Annie-Docs/actions)
[![CI Status](https://img.shields.io/github/actions/workflow/status/Programmers-Paradise/Annie-Docs/ci.yml?branch=main&label=CI)](https://github.com/Programmers-Paradise/Annie-Docs/actions)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/Programmers-Paradise/Annie-Docs/codeql.yml?branch=main&label=CodeQL)](https://github.com/Programmers-Paradise/Annie-Docs/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Security](https://img.shields.io/badge/Security-Policy-red.svg)](SECURITY.md)
[![Main Repo](https://img.shields.io/badge/source-Annie-green)](https://github.com/Programmers-Paradise/Annie)

> **Official documentation for Annie - Blazingly fast Approximate Nearest Neighbors in Rust**

This repository contains the source code and automation for [annie-docs.netlify.app](https://annie-docs.netlify.app/), the comprehensive documentation site for the Annie library.

---

## Quick Navigation

| Resource                  | Description                       | Link                                                                          |
| ------------------------- | --------------------------------- | ----------------------------------------------------------------------------- |
| **Live Documentation** | Complete API docs & guides        | [annie-docs.netlify.app](https://annie-docs.netlify.app/)                     |
| **Annie Library**      | Main source code repository       | [GitHub](https://github.com/Programmers-Paradise/Annie)                       |
| **PyPI Package**       | Install Annie via pip             | [rust-annie](https://pypi.org/project/rust-annie/)                            |
| **Report Doc Issues**  | Documentation bugs & improvements | [Issues](https://github.com/Programmers-Paradise/Annie-Docs/issues)           |
| **Community**          | Questions & discussions           | [Discussions](https://github.com/Programmers-Paradise/Annie-Docs/discussions) |

---

## Repository Structure

```
annie-docs/
├── docs/                    # Documentation content (Markdown)
│   ├── index.md               # Homepage
│   ├── api/                   # API reference docs
│   │   ├── ann_index.md       # ANN Index API
│   │   ├── hnsw_index.md      # HNSW Index API
│   │   └── threadsafe_index.md # ThreadSafe Index API
│   ├── examples.md            # Usage examples
│   ├── filtering.md           # Filtering guide
│   ├── concurrency.md         # Concurrency documentation
│   └── ...                   # Additional guides
├── scripts/               # Build & deployment automation
│   ├── build-docs.sh         # Build documentation
│   ├── deploy.sh             # Deploy to production
│   ├── serve-public.sh       # Local network sharing
│   ├── sync-api-docs.py      # Auto-sync API docs
│   ├── sync-readme-content.py # Auto-sync README content
│   └── update-version-info.py # Auto-update version info
├── configs/               # Platform configurations
│   ├── netlify.toml          # Netlify deployment
│   └── CNAME                 # Custom domain config
├── .github/workflows/     # CI/CD automation
│   ├── deploy-docs.yml       # Auto-deployment
│   ├── sync-docs.yml         # Auto-sync from main repo
│   ├── ci.yml                # Continuous integration
│   ├── codeql.yml            # Security analysis
│   └── dependencies.yml     # Dependency updates
├── docs-management/       # Setup & deployment guides
│   ├── CONTRIBUTING.md       # Contribution guidelines
│   ├── FILE-ORGANIZATION.md  # Repository structure guide
│   └── SETUP-SUMMARY.md      # Complete setup summary
├── mkdocs.yml             # MkDocs configuration
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
├── SECURITY.md            # Security policy
└── README.md              # This file
```

---

## Local Development

### Quick Start

```bash
# Clone documentation repository
git clone https://github.com/Programmers-Paradise/Annie-Docs.git
cd Annie-Docs

# Build documentation (creates venv, installs deps, builds site)
./scripts/build-docs.sh

# Serve locally with live reload
source venv/bin/activate
mkdocs serve
```

Visit `http://localhost:8000` to see your local documentation.

### Available Scripts

| Script                      | Purpose               | Usage                 |
| --------------------------- | --------------------- | --------------------- |
| `./scripts/build-docs.sh`   | Build documentation   | One-command setup     |
| `./scripts/serve-public.sh` | Share on network      | `http://YOUR-IP:8080` |
| `./scripts/deploy.sh`       | Production deployment | Build + optimization  |
| `./scripts/tunnel.sh`       | Temporary public URL  | Requires ngrok        |

---

## Automatic Synchronization

This documentation repository automatically syncs with the [main Annie library](https://github.com/Programmers-Paradise/Annie):

### How It Works

1. **Changes in Annie repo** → Triggers webhook/repository dispatch
2. **GitHub Action runs** → Pulls latest docs, examples, and API references
3. **Documentation updates** → Rebuilds and redeploys annie.io
4. **Site goes live** → Updates visible within minutes

### What Gets Synced

- **API documentation** from Rust/Python docstrings
- **Examples** from `/examples` directory
- **README** content and project guides
- **Version information** from Cargo.toml
- **Documentation** from main repo's `/docs` folder

### Setup Auto-Sync

To enable automatic syncing, see the complete guide: [**docs-management/SETUP-SUMMARY.md**](docs-management/SETUP-SUMMARY.md)

This involves:

1. Adding a workflow to your main Annie repository
2. Creating a GitHub personal access token
3. Configuring the token as a repository secret

---

## Deployment

### Current Deployment

The documentation is automatically deployed to: **[annie-docs.netlify.app](https://annie-docs.netlify.app/)**

### Automatic Deployment

The site automatically deploys when you push to the `main` branch:

1. **Push to GitHub** → Triggers build
2. **MkDocs builds** → Generates static site  
3. **Netlify deploys** → Site goes live

### Manual Deployment

```bash
git push origin main  # Triggers automatic deployment
```

For detailed deployment instructions, see: [**docs-management/SETUP-SUMMARY.md**](docs-management/SETUP-SUMMARY.md)

---

## Contributing

### Quick Contribution

1. **Fork** this repository
2. **Clone** your fork locally
3. **Create** a feature branch
4. **Edit** documentation in `docs/` directory
5. **Test** with `mkdocs serve`
6. **Submit** a pull request

For detailed guidelines, see [docs-management/CONTRIBUTING.md](docs-management/CONTRIBUTING.md).

---

## License

This documentation repository is licensed under the **MIT License**.

---

## Support & Help

| Issue Type               | Where to Go                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------ |
| **Documentation bugs**   | [Create Issue](https://github.com/Programmers-Paradise/Annie-Docs/issues)            |
| **Security vulnerabilities** | [Security Policy](SECURITY.md)                                                    |
| **Usage questions**      | [GitHub Discussions](https://github.com/Programmers-Paradise/Annie-Docs/discussions) |
| **Annie library issues** | [Main Repository](https://github.com/Programmers-Paradise/Annie/issues)              |

---

<div align="center">

**[Visit annie-docs.netlify.app](https://annie-docs.netlify.app/)** • **[Get Started](https://annie-docs.netlify.app/#installation)** • **[Contribute](docs-management/CONTRIBUTING.md)**

---

_Powered by MkDocs • Hosted on Netlify • Made with care by the Annie team_

</div>
