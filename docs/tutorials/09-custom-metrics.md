# 9. Custom Distance Metrics

**Estimated time:** 12 minutes

Learn how to define and use custom distance metrics in Annie.

## Steps
1. **Define a custom metric:**
   - Subclass or configure as per API.
2. **Use with AnnIndex:**
   - Pass your metric to the index constructor.

## Example
```python
from rust_annie import AnnIndex, Distance
index = AnnIndex(128, Distance.COSINE)
```

## Next: [GPU Acceleration](10-gpu-usage.md)
