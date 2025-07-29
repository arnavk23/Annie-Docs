# 2. Indexing Your First Dataset

**Estimated time:** 7 minutes

Learn how to add data to your Annie index.

## Steps
1. **Prepare your data:**
   ```python
   import numpy as np
   data = np.random.rand(1000, 128).astype(np.float32)
   ids = np.arange(1000, dtype=np.int64)
   ```
2. **Add data to the index:**
   ```python
   from rust_annie import AnnIndex, Distance
   index = AnnIndex(128, Distance.EUCLIDEAN)
   index.add(data, ids)
   print("Data added!")
   ```

## Next: [Performing Your First Search](03-basic-search.md)
