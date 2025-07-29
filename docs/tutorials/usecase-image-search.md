# Use Case: Image Search with Annie

**Estimated time:** 12 minutes

Learn how to use Annie for image similarity search.

## Steps
1. **Extract image embeddings (e.g., with a neural network)**
2. **Index embeddings**
3. **Query with a new image embedding**
4. **Return similar images**

## Example
```python
# Index image embeddings
index.add(image_embeddings, image_ids)
# Query with new image
similar_images, _ = index.search(query_embedding, k=5)
```

---

For more, see [examples.md](../examples.md).
