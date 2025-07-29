# 11. Performance Optimization

**Estimated time:** 12 minutes

Learn how to tune Annie for maximum performance.

## Topics
- Index parameter tuning
- Batch operations
- Memory and resource usage
- Profiling and monitoring

## Example
```python
# Adjust index parameters for your workload
index = AnnIndex(128, Distance.EUCLIDEAN, ef_search=100, ef_construction=200)
```

---

For more, see [Performance FAQ](../faq.md#performance-tuning).
