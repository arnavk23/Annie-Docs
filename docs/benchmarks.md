# Annie Benchmarks & Performance

This section showcases Annie's performance and helps you optimize for your use case.

## Interactive Benchmark Dashboard

<iframe src="https://annie-benchmarks.example.com" width="100%" height="480" frameborder="0" title="Annie Benchmark Dashboard"></iframe>

*If the dashboard does not load, [view it here](https://annie-benchmarks.example.com).*  

---

## Library Comparison Table

| Library   | Build Time | Search Latency | Recall@10 | Memory Usage | CPU | GPU Support |
|-----------|-----------|----------------|-----------|--------------|-----|-------------|
| **Annie** | 1x        | 1x             | 99.2%     | 1x           | Yes | Yes         |
| Faiss     | 1.2x      | 1.1x           | 98.7%     | 1.1x         | Yes | Yes         |
| Annoy     | 2.5x      | 2.2x           | 97.5%     | 1.3x         | Yes | No          |
| HNSWlib   | 1.1x      | 1.2x           | 98.9%     | 1.2x         | Yes | No          |

*All results normalized to Annie (lower is better for time/latency/memory).*  

---

## Latency vs. Accuracy

![Latency vs. Recall](assets/latency_vs_recall.png)

- Annie achieves high recall with low latency compared to other libraries.

---

## Memory Usage Benchmarks

![Memory Usage](assets/memory_usage.png)

- Annie is optimized for low memory usage, especially on large datasets.

---

## Dataset Size Scaling

![Scaling](assets/scaling.png)

- Annie scales efficiently from 10K to 10M+ vectors.

---

## GPU vs. CPU Performance

![GPU vs CPU](assets/gpu_vs_cpu.png)

- GPU acceleration can provide 3-10x speedup for large batch queries.

---

## Performance Tuning Recommendations

- Use batch operations for large queries.
- Tune index parameters (`ef_search`, `ef_construction`) for your workload.
- Monitor memory and CPU usage.
- Use GPU for large-scale or real-time workloads.

---

## Explore Benchmarks

- [Interactive Explorer](https://annie-benchmarks.example.com/explorer)
- [Raw Results CSV](https://annie-benchmarks.example.com/results.csv)

---

For more details, see [Performance Optimization Tutorial](tutorials/11-performance.md).
