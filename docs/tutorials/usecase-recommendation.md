# Use Case: Building a Recommendation System

**Estimated time:** 15 minutes

Learn how to use Annie to build a simple recommendation system.

## Steps
1. **Prepare user/item vectors**
2. **Index items**
3. **Query with user vector**
4. **Return top recommendations**

## Example
```python
# Index item vectors
index.add(item_vectors, item_ids)
# Query with user vector
recommendations, _ = index.search(user_vector, k=10)
```

---

For more use cases, see [examples.md](../examples.md).
