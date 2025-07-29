# Troubleshooting Guide

This guide helps you resolve common installation, build, and runtime issues with Annie and its documentation.

## Installation Issues
- **'No module named rust_annie'**
  - Ensure you installed with the correct Python version: `pip install rust-annie`
  - Check your virtual environment is activated.
- **Rust or maturin not found**
  - Install Rust: https://rustup.rs
  - Install maturin: `pip install maturin`

## Build Errors
- **Error: MkDocs encountered an error parsing the configuration file**
  - Check for YAML syntax errors in `mkdocs.yml`.
  - Ensure all required dependencies are installed: `pip install -r requirements.txt`
- **'Unrecognised theme name: material'**
  - Run `pip install mkdocs-material`.
- **'No module named pymdownx'**
  - Run `pip install pymdown-extensions`.

## Runtime Errors
- **'Index shape mismatch'**
  - Ensure your data shape matches the index dimensions.
- **'Out of memory'**
  - Reduce batch size or use a machine with more RAM.

## Performance Tuning
- Use batch operations for large datasets.
- Adjust index parameters for your workload.
- Monitor memory and CPU usage during large operations.

## Compatibility
- See the [FAQ](faq.md#compatibility-matrix) for supported OS and Python versions.

## Migration
- See the FAQ below for tips on migrating from other ANN libraries.

---

If your issue is not listed, please open an issue and include error messages and environment details.
