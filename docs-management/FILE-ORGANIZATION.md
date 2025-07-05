# Annie.io Documentation - File Organization

## Directory Structure

```
annie-docs/
├── docs/                    # Main documentation content
│   ├── index.md               # Homepage
│   ├── api/                   # API reference docs
│   │   ├── ann_index.md       # ANN Index API
│   │   ├── hnsw_index.md      # HNSW Index API
│   │   └── threadsafe_index.md # ThreadSafe Index API
│   ├── examples.md            # Usage examples
│   ├── filtering.md           # Filtering documentation
│   ├── concurrency.md         # Concurrency guide
│   └── contributing.md        # How to contribute
├── scripts/               # Build and deployment scripts
│   ├── build-docs.sh         # Build documentation
│   ├── deploy.sh             # Deploy to production
│   ├── serve-public.sh       # Serve on network
│   ├── tunnel.sh             # Create public tunnel
│   ├── sync-api-docs.py      # Sync API docs from main repo
│   ├── sync-readme-content.py # Sync README content
│   └── update-version-info.py # Update version information
├── configs/               # Configuration files
│   ├── netlify.toml          # Netlify deployment
│   └── CNAME                 # Custom domain configuration
├── .github/workflows/     # GitHub Actions automation
│   ├── deploy-docs.yml       # Auto-deployment workflow
│   ├── sync-docs.yml         # Auto-sync from main repo
│   ├── ci.yml                # Continuous integration
│   ├── codeql.yml            # Security analysis
│   └── dependencies.yml     # Dependency updates
├── docs-management/       # Repository management docs
│   ├── CONTRIBUTING.md       # Contribution guidelines
│   ├── FILE-ORGANIZATION.md  # This file
│   └── SETUP-SUMMARY.md      # Complete setup summary
├── site/                  # Generated static site (MkDocs output)
├── venv/                  # Python virtual environment
├── mkdocs.yml             # MkDocs configuration
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # MIT License
└── SECURITY.md            # Security policy
```

## File Purposes

### Core Files

- **`mkdocs.yml`** - Main configuration for documentation generation
- **`requirements.txt`** - Python dependencies for building docs
- **`README.md`** - Project overview and setup instructions

### Documentation Content (`docs/`)

- **`index.md`** - Main homepage content
- **`api/`** - Complete API reference documentation
- **`examples.md`** - Usage examples and tutorials
- **`contributing.md`** - Contribution guidelines

### Build Scripts (`scripts/`)

- **`build-docs.sh`** - One-command documentation building
- **`deploy.sh`** - Production deployment preparation
- **`serve-public.sh`** - Share docs on local network
- **`tunnel.sh`** - Create temporary public URLs

### Configuration (`configs/`)

- **`netlify.toml`** - Netlify platform configuration
- **`CNAME`** - Custom domain configuration for GitHub Pages

### Automation (`.github/workflows/`)

- **`deploy-docs.yml`** - Automatic deployment on git push
- **`sync-docs.yml`** - Auto-sync documentation from main Annie repository
- **`ci.yml`** - Continuous integration (linting, testing, quality checks)
- **`codeql.yml`** - Security analysis and vulnerability scanning
- **`dependencies.yml`** - Automated dependency updates

### Legal & Security

- **`LICENSE`** - MIT License for the documentation repository
- **`SECURITY.md`** - Security policy and vulnerability reporting guidelines

## Quick Commands

```bash
# Build documentation
./scripts/build-docs.sh

# Serve locally for development
source venv/bin/activate && mkdocs serve

# Serve on network for sharing
./scripts/serve-public.sh

# Deploy to production
./scripts/deploy.sh

# Create temporary public URL
./scripts/tunnel.sh
```

## File Management Rules

### Edit These Files:

- `docs/` - All documentation content
- `mkdocs.yml` - Site configuration
- `README.md` - Project information
- Scripts in `scripts/` - Build automation

### Don't Edit These:

- `site/` - Auto-generated, will be overwritten
- `venv/` - Python virtual environment
- `.git/` - Git repository data

### Be Careful With:

- `.github/workflows/` - Changes affect auto-deployment
- `configs/` - Platform-specific deployment settings

## Workflow

1. **Edit content** in `docs/` directory
2. **Test locally** with `mkdocs serve`
3. **Build** with `./scripts/build-docs.sh`
4. **Commit and push** to trigger auto-deployment
5. **Check deployment** in GitHub Actions tab

This organization keeps the repository clean and makes it easy to find and manage documentation files.
