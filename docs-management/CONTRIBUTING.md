# Contributing to Annie Documentation

Thank you for your interest in contributing to Annie's documentation! This guide will help you get started with contributing to our documentation site.


## Table of Contents

- [Getting Started](#getting-started)
- [Documentation Structure](#documentation-structure)
- [Setting Up Development Environment](#setting-up-development-environment)
- [Making Changes](#making-changes)
- [Writing Guidelines](#writing-guidelines)
- [Documentation Standards and Templates](#documentation-standards-and-templates)
- [Submitting Changes](#submitting-changes)
- [Review Process](#review-process)

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- Text editor or IDE

### Quick Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Annie-Docs.git
   cd Annie-Docs
   ```

2. **Build Documentation**
   ```bash
   ./build-docs.sh
   ```

3. **Start Development Server**
   ```bash
   source venv/bin/activate
   mkdocs serve
   ```

4. **Open in Browser**
   Visit `http://localhost:8000` to see your changes live.

## Documentation Structure

```
docs/
├── index.md              # Homepage
├── api/                  # API Reference
│   ├── ann_index.md     # AnnIndex class
│   ├── hnsw_index.md    # PyHnswIndex class
│   └── threadsafe_index.md
├── examples.md           # Usage examples
├── concurrency.md        # Thread-safety features
└── filtering.md          # Filtered search
```


## Documentation Standards and Templates

Please follow these resources for all documentation contributions:

- [Documentation Style Guide](DOCUMENTATION-STYLE-GUIDE.md): Formatting, structure, and tone standards.
- [Writing Guidelines](WRITING-GUIDELINES.md): Steps and best practices for writing docs.
- [Screenshot and Image Guidelines](SCREENSHOT-GUIDELINES.md): How to add and format images.
- [Accessibility Guidelines](ACCESSIBILITY-GUIDELINES.md): Ensure docs are usable by everyone.
- [Review Checklist](REVIEW-CHECKLIST.md): Use before submitting docs for review.
- [Content Lifecycle](CONTENT-LIFECYCLE.md): How docs are planned, reviewed, and maintained.
- [Maintenance Procedures](MAINTENANCE-PROCEDURES.md): Keeping docs up-to-date.
- [New Doc Template](TEMPLATE-NEW-DOC.md) and [Update Template](TEMPLATE-DOC-UPDATE.md): For new or updated docs.

Refer to these guides and templates to ensure your contributions meet project standards.

### Manual Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build site
mkdocs build

# Serve locally with auto-reload
mkdocs serve --dev-addr=0.0.0.0:8000
```

### Using Scripts

```bash
# Build documentation
./build-docs.sh

# Deploy (build + prepare for hosting)
./deploy.sh
```

## Making Changes

### Types of Contributions

1. **Bug Fixes**: Typos, broken links, formatting issues
2. **Content Updates**: New examples, clarifications, additional details
3. **New Documentation**: New features, API additions
4. **Structure Improvements**: Navigation, organization, user experience


### Workflow

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-branch-name
   ```

2. **Make Your Changes**
   - Edit files in the `docs/` directory
   - Use Markdown syntax
   - Follow the [Documentation Style Guide](DOCUMENTATION-STYLE-GUIDE.md) and [Writing Guidelines](WRITING-GUIDELINES.md)
   - Use the [New Doc Template](TEMPLATE-NEW-DOC.md) or [Update Template](TEMPLATE-DOC-UPDATE.md) as appropriate

3. **Test Locally**
   ```bash
   mkdocs serve
   ```
   Visit `http://localhost:8000` to review changes

4. **Build and Verify**
   ```bash
   mkdocs build
   ```
   Ensure no build errors


## Writing Guidelines

See [Writing Guidelines](WRITING-GUIDELINES.md) and [Documentation Style Guide](DOCUMENTATION-STYLE-GUIDE.md) for detailed standards, formatting, and examples. For screenshots and images, see [Screenshot and Image Guidelines](SCREENSHOT-GUIDELINES.md). For accessibility, see [Accessibility Guidelines](ACCESSIBILITY-GUIDELINES.md).

## Submitting Changes


### Before Submitting

1. **Test Your Changes**
   ```bash
   mkdocs build  # Check for build errors
   mkdocs serve  # Test locally
   ```

2. **Check Links**
   - Ensure all internal links work
   - Verify external links are accessible

3. **Review Content**
   - Proofread for typos and grammar
   - Ensure code examples work
   - Check formatting consistency
   - Complete the [Review Checklist](REVIEW-CHECKLIST.md)
   - Ensure accessibility and image guidelines are followed

### Creating a Pull Request

1. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "docs: improve examples in filtering.md"
   ```

2. **Push to Your Fork**
   ```bash
   git push origin feature/improve-examples
   ```

3. **Create Pull Request**
   - Go to GitHub and create a pull request
   - Use a descriptive title
   - Explain what you changed and why
   - Reference any related issues

### Pull Request Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix (typo, broken link, etc.)
- [ ] Content update (new examples, clarifications)
- [ ] New documentation (new features)
- [ ] Structure improvement

## Testing
- [ ] Built successfully with `mkdocs build`
- [ ] Tested locally with `mkdocs serve`
- [ ] Checked all links work
- [ ] Verified code examples run

## Screenshots (if applicable)
Add screenshots of significant visual changes.
```


## Review Process

All documentation changes are reviewed for:

1. **Accuracy**: Information is correct and up-to-date
2. **Clarity**: Content is easy to understand
3. **Completeness**: Examples work and are comprehensive
4. **Consistency**: Follows [Documentation Style Guide](DOCUMENTATION-STYLE-GUIDE.md)
5. **Accessibility**: Follows [Accessibility Guidelines](ACCESSIBILITY-GUIDELINES.md)
6. **Value**: Genuinely helpful to users

Use the [Review Checklist](REVIEW-CHECKLIST.md) before submitting.

---

For more on the documentation lifecycle and maintenance, see [Content Lifecycle](CONTENT-LIFECYCLE.md) and [Maintenance Procedures](MAINTENANCE-PROCEDURES.md).

## Issue Labels

When creating issues, use these labels:

- `documentation` - General documentation issues
- `bug` - Errors in docs (typos, broken links)
- `enhancement` - Improvements to existing content
- `new-content` - Requests for new documentation
- `good-first-issue` - Good for newcomers

## Getting Help

- **GitHub Discussions**: Ask questions about contributing
- **Issues**: Report bugs or request features
---

Thank you for helping make Annie's documentation better!
