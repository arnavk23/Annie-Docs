# Contributing to Annie Documentation

Thank you for your interest in contributing to Annie's documentation! This guide will help you get started with contributing to our documentation site.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Documentation Structure](#documentation-structure)
- [Setting Up Development Environment](#setting-up-development-environment)
- [Making Changes](#making-changes)
- [Writing Guidelines](#writing-guidelines)
- [Submitting Changes](#submitting-changes)
- [Review Process](#review-process)

## 🚀 Getting Started

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

## 📁 Documentation Structure

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

## 🛠 Setting Up Development Environment

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

## ✏️ Making Changes

### Types of Contributions

1. **Bug Fixes**: Typos, broken links, formatting issues
2. **Content Updates**: New examples, clarifications, additional details
3. **New Documentation**: New features, API additions
4. **Structure Improvements**: Navigation, organization, user experience

### Workflow

1. **Create a Branch**
   ```bash
   git checkout -b feature/improve-examples
   ```

2. **Make Your Changes**
   - Edit files in the `docs/` directory
   - Use Markdown syntax
   - Follow our writing guidelines

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

## 📝 Writing Guidelines

### Markdown Standards

- Use `#` for main headings, `##` for sections, `###` for subsections
- Use code blocks with language specification:
  ```python
  # Good
  import numpy as np
  ```
- Use `**bold**` for emphasis, `*italic*` for secondary emphasis
- Use backticks for `inline code` and class names like `AnnIndex`

### Code Examples

- **Complete Examples**: Show full working code
- **Clear Comments**: Explain what each section does
- **Realistic Data**: Use meaningful variable names and realistic scenarios
- **Error Handling**: Include error handling where appropriate

```python
# Good example
import numpy as np
from rust_annie import AnnIndex, Distance

# Create index for 128-dimensional vectors
index = AnnIndex(128, Distance.EUCLIDEAN)

# Add sample data
data = np.random.rand(1000, 128).astype(np.float32)
ids = np.arange(1000, dtype=np.int64)
index.add(data, ids)

# Search for nearest neighbors
query = np.random.rand(128).astype(np.float32)
neighbor_ids, distances = index.search(query, k=5)
print(f"Found {len(neighbor_ids)} neighbors")
```

### API Documentation

- **Class Descriptions**: Clear purpose and use cases
- **Parameter Details**: Type, description, constraints
- **Return Values**: What the method returns
- **Examples**: Show typical usage
- **Error Conditions**: When methods might fail

### Writing Style

- **Clear and Concise**: Get to the point quickly
- **Beginner-Friendly**: Explain concepts that might be unfamiliar
- **Consistent Terminology**: Use the same terms throughout
- **Active Voice**: "Create an index" vs "An index is created"

## 📤 Submitting Changes

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

## 🔍 Review Process

### What We Look For

1. **Accuracy**: Information is correct and up-to-date
2. **Clarity**: Content is easy to understand
3. **Completeness**: Examples work and are comprehensive
4. **Consistency**: Follows existing style and structure
5. **Value**: Genuinely helpful to users

### Review Timeline

- **Initial Review**: Within 2-3 days
- **Feedback**: We'll provide specific suggestions
- **Approval**: Once all feedback is addressed

### After Approval

- Changes are merged to `main` branch
- Documentation is automatically deployed
- Your contribution is credited

## 🏷️ Issue Labels

When creating issues, use these labels:

- `documentation` - General documentation issues
- `bug` - Errors in docs (typos, broken links)
- `enhancement` - Improvements to existing content
- `new-content` - Requests for new documentation
- `good-first-issue` - Good for newcomers

## 💬 Getting Help

- **GitHub Discussions**: Ask questions about contributing
- **Issues**: Report bugs or request features
- **Email**: Contact maintainers directly

## 🎉 Recognition

Contributors are recognized in:
- GitHub contributors list
- Release notes for significant contributions
- Special mentions for major improvements

---

Thank you for helping make Annie's documentation better! 🚀
