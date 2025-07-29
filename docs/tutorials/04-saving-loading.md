# 4. Saving and Loading Indexes

**Estimated time:** 6 minutes

Learn how to save your index to disk and load it later.

## Steps
1. **Save the index:**
   ```python
   index.save("my_index.ann")
   ```
2. **Load the index:**
   ```python
   from rust_annie import AnnIndex
   index = AnnIndex.load("my_index.ann")
   print("Index loaded!")
   ```

## Next: [Batch Operations](05-batch-operations.md)
