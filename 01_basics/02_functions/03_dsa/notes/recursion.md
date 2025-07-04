# 📘 Recursion Notes

- A function that calls itself
- Must have a base case to avoid infinite calls
- Example: Factorial, Fibonacci, Tower of Hanoi

## Example: Factorial

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
