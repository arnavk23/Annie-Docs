# 5. Batch Operations

**Estimated time:** 8 minutes

Learn how to add and search multiple vectors efficiently.

## Steps
1. **Batch add data:**
   ```python
   index.add(data, ids)
   ```
2. **Batch search:**
   ```python
   queries = np.random.rand(10, 128).astype(np.float32)
   results = index.batch_search(queries, k=5)
   print(results)
   ```

## Next: [Using Annie in Production](06-production-usage.md)
