# Annie.io

Blazingly fast Approximate Nearest Neighbors in Rust

## Installation



```bash
# Stable release from PyPI:
pip install rust-annie

# Or install from source (requires Rust toolchain + maturin):
git clone https://github.com/yourusername/rust_annie.git
cd rust_annie
pip install maturin
maturin develop --release
```

## Basic Usage



```python
import numpy as np
from rust_annie import AnnIndex, Distance

# Create an 8-dim Euclidean index
idx = AnnIndex(8, Distance.EUCLIDEAN)

# Add 100 random vectors
data = np.random.rand(100, 8).astype(np.float32)
ids  = np.arange(100, dtype=np.int64)
idx.add(data, ids)

# Query one vector
labels, dists = idx.search(data[0], k=5)
print("Nearest IDs:", labels)
print("Distances :", dists)
```

## Key Features



- **Ultra-fast brute-force** k-NN search (Euclidean, Cosine, Manhattan, Chebyshev)  
- **Batch** queries over multiple vectors  
- **Thread-safe** wrapper with GIL release for true concurrency  
- **Zero-copy** NumPy integration (via PyO3 & rust-numpy)  
- **On-disk** persistence with bincode + serde  
- **Multi-platform** wheels (manylinux, musllinux, Windows, macOS)  
- **Automated CI** with correctness & performance checks

## Navigation

- [API Reference](api/ann_index.md) - Core classes and methods
- [Examples](examples.md) - Usage examples and tutorials
- [Concurrency](concurrency.md) - Thread-safe operations
- [Filtering](filtering.md) - Custom search filters

## Quick Links

- [GitHub Repository](https://github.com/Programmers-Paradise/Annie)
- [PyPI Package](https://pypi.org/project/rust-annie/)
- [Benchmark Results](https://programmers-paradise.github.io/Annie/)
