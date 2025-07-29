# 7. Filtering and Metadata

**Estimated time:** 10 minutes

Learn how to use filtering and attach metadata to your vectors.

## Steps
1. **Add metadata to vectors:**
   - Use the `add` method with metadata if supported.
2. **Filter during search:**
   - Use filter parameters to restrict search results.

## Example
```python
# Example assumes filtering API is available
results = index.search(query, k=5, filter={"category": "A"})
```

## Next: [Debugging and Troubleshooting](08-debugging.md)
