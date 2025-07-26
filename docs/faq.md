# Frequently Asked Questions (FAQ)

Welcome to the Annie FAQ! Use your browser's search (Ctrl+F) to quickly find answers. Questions are grouped by category for easy navigation.

## General
- **What is Annie?**
  - Annie is a fast Approximate Nearest Neighbors (ANN) library written in Rust with Python bindings.
- **Who maintains Annie?**
  - Annie is maintained by the Programmers-Paradise community.

## Installation & Setup
- **How do I install Annie?**
  - See the [installation guide](index.md#installation) or run `pip install rust-annie`.
- **I get a 'No module named rust_annie' error.**
  - Ensure you installed the package in the correct Python environment and that your Python version is supported.
- **Which Python versions are supported?**
  - See the [compatibility matrix](faq.md#compatibility-matrix).

## Troubleshooting
- **Build fails with 'cargo' or 'maturin' errors.**
  - Ensure Rust and maturin are installed. See [troubleshooting](troubleshooting.md#build-errors).
- **Documentation site won't build.**
  - Make sure all requirements in `requirements.txt` are installed.

## Performance & Tuning
- **How can I speed up indexing/search?**
  - Use batch operations and tune index parameters. See [performance FAQ](faq.md#performance-tuning).
- **How much memory does Annie use?**
  - See [resource usage](faq.md#memory-and-resource-usage).

## Error Messages
- **'Index shape mismatch' error.**
  - Check that your data shape matches the index dimensions.
- **'Out of memory' error.**
  - Reduce batch size or use a machine with more RAM.

## Migration
- **How do I migrate from Faiss/Annoy/HNSW?**
  - See [migration guide](faq.md#migration-guides).

## Compatibility Matrix
| OS           | Python 3.8 | Python 3.9 | Python 3.10 | Python 3.11 |
|--------------|------------|------------|-------------|-------------|
| Linux        | ✓          | ✓          | ✓           | ✓           |
| macOS (x86)  | ✓          | ✓          | ✓           | ✓           |
| macOS (M1)   | ✓          | ✓          | ✓           | ✓           |
| Windows      | ✓          | ✓          | ✓           | ✓           |

## Memory and Resource Usage
- Annie is optimized for low memory usage, but large datasets require more RAM. Monitor usage and adjust batch sizes as needed.

## Issue Template Integration
- When opening an issue, please check the FAQ for solutions. The issue template will prompt you to confirm this.

---

For more troubleshooting, see [troubleshooting.md](troubleshooting.md).
