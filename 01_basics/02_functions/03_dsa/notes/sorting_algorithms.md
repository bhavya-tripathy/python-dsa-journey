
#### `sorting_algorithms.md`
```markdown
# 📘 Sorting Algorithms

### 🔁 Bubble Sort (O(n²))

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
