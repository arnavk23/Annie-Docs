# 3. Performing Your First Search

**Estimated time:** 7 minutes

Learn how to search for nearest neighbors in your index.

## Steps
1. **Create a query vector:**
   ```python
   query = np.random.rand(128).astype(np.float32)
   ```
2. **Search the index:**
   ```python
   neighbor_ids, distances = index.search(query, k=5)
   print("Neighbors:", neighbor_ids)
   ```

## Next: [Saving and Loading Indexes](04-saving-loading.md)
