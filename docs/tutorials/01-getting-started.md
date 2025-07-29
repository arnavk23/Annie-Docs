# 1. Getting Started with Annie

**Estimated time:** 5 minutes

This tutorial will help you install Annie and run your first nearest neighbor search.

## Prerequisites
- Python 3.8+
- pip

## Steps
1. **Install Annie:**
   ```bash
   pip install rust-annie
   ```
2. **Import and check version:**
   ```python
   import rust_annie
   print(rust_annie.__version__)
   ```
3. **Create a simple index:**
   ```python
   from rust_annie import AnnIndex, Distance
   index = AnnIndex(128, Distance.EUCLIDEAN)
   print("Index created!")
   ```

## Next: [Indexing Your First Dataset](02-indexing-basics.md)
