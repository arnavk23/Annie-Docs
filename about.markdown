---
layout: page
title: About
permalink: /about/
---

# About Annie.io

This is the documentation site for **Annie** - a blazingly fast Approximate Nearest Neighbors library implemented in Rust with Python bindings.

## Documentation System

This site uses **MkDocs** for documentation generation. The main documentation is located in the `docs/` folder and built to the `site/` directory.

## Project Links

- [GitHub Repository](https://github.com/Programmers-Paradise/Annie)
- [PyPI Package](https://pypi.org/project/rust-annie/)
- [Live Documentation](https://annie.io)

## Building Documentation

To build the documentation locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Build the site
mkdocs build

# Serve locally  
mkdocs serve
```

Or use the convenience script:

```bash
./build-docs.sh
```
