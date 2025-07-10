

### ✅ 1. **Prime Number Check**

```python
def is_prime(n):
    if n < 2:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5)+1):  # Only check up to sqrt(n)
        if n % i == 0:
            return False  # If divisible, not prime
    return True
```

**🔍 Logic:**

* A number is **prime** if it has **no divisors other than 1 and itself**.
* We check for divisibility from `2` to `√n`. Why?

  * Because if `n = a × b`, one of them must be ≤ √n.
* If any such `i` divides `n` evenly (`n % i == 0`), it’s **not prime**.

---

### ✅ 2. **Factorial**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive case
```

**🔍 Logic:**

* The factorial of `n` (`n!`) is `n × (n-1) × (n-2) ... × 1`.
* We define this **recursively**:

  * `factorial(n) = n * factorial(n-1)`
  * Until we reach base case `factorial(0)` or `factorial(1)` = `1`.

---

### ✅ 3. **Fibonacci (Recursive)**

```python
def fibonacci(n):
    if n <= 1:
        return n  # Base case
    return fibonacci(n-1) + fibonacci(n-2)  # Recursive case
```

**🔍 Logic:**

* Fibonacci sequence: `0, 1, 1, 2, 3, 5, 8, 13, ...`
* Formula: `F(n) = F(n-1) + F(n-2)`
* Base cases:

  * `F(0) = 0`
  * `F(1) = 1`
* Then builds up using previous two numbers.

> ⚠️ This method is slow for large `n` (exponential time) — we can optimize using **memoization** or **iteration** later.

---

### ✅ 4. **Sum of Variable Arguments**

```python
def sum_all(*args):
    return sum(args)
```

**🔍 Logic:**

* `*args` lets us pass **any number of arguments** into the function.
* `args` becomes a **tuple** like `(1, 2, 3, 4)`.
* We use Python’s built-in `sum()` to add them all.

> ✅ Flexible, clean, and commonly used in real-world Python code.

---

### ✅ 5. **Lambda Function to Double List**

```python
double = lambda lst: [x*2 for x in lst]
```

**🔍 Logic:**

* `lambda` defines a small **anonymous function** (no `def`, no name).
* Input: `lst` → a list of numbers.
* Output: a **new list** with each number multiplied by 2.

Example:

```python
double([1, 2, 3])  # Output: [2, 4, 6]
```

> ⚡ Super useful in one-liner transformations or with `map()`/`filter()`.

---

### ✅ 6. **Palindrome Checker**

```python
def is_palindrome(s):
    return s == s[::-1]
```

**🔍 Logic:**

* A **palindrome** reads the same forwards and backwards.
* `s[::-1]` is Python's slicing to reverse a string.
* So, we check:

  * Is the original string equal to its reversed version?

Example:

```python
is_palindrome("madam")  # True
is_palindrome("apple")  # False
```

---

### ✅ Summary Table:

| Function        | Concept                | Technique             | Key Idea                |
| --------------- | ---------------------- | --------------------- | ----------------------- |
| `is_prime`      | Number theory          | Loop till √n          | Efficient prime check   |
| `factorial`     | Recursion              | Base + recursive case | Classic factorial logic |
| `fibonacci`     | Recursion              | Two base cases        | Sum of previous two     |
| `sum_all`       | \*args                 | Tuple unpacking       | Flexible input          |
| `lambda`        | Functional programming | List comprehension    | Short anonymous func    |
| `is_palindrome` | String manipulation    | Slice reversal        | One-liner logic         |

