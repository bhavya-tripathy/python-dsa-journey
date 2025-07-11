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
# Recursion in Python

## What is Recursion?
A function that **calls itself** to solve a smaller instance of the same problem.

## Structure of a Recursive Function
1. **Base Case**: Stops the recursion.
2. **Recursive Case**: Function calls itself with simpler input.

## Example:
```python
def factorial(n):
    if n == 0:
        return 1   # Base case
    return n * factorial(n - 1)  # Recursive case
