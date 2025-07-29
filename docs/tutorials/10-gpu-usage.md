# 10. GPU Acceleration

**Estimated time:** 15 minutes

Learn how to use GPU acceleration with Annie (if supported).

## Steps
1. **Check GPU support:**
   - Ensure your hardware and drivers are compatible.
2. **Enable GPU usage:**
   - Set the appropriate flag or environment variable.

## Example
```python
# Example only if GPU support is available
index = AnnIndex(128, Distance.EUCLIDEAN, use_gpu=True)
```

## Next: [Performance Optimization](11-performance.md)
