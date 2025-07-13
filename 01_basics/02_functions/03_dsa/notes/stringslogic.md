Here's your full lesson on **Strings in Python**, converted into a clean, elegant `strings.md` markdown file for your repo:

---

````markdown
# 🧵 Python Strings – Masterclass

---

## 🔹 1. What is a String?

A **string** is a sequence of characters. In Python, anything inside quotes is a string:

```python
s1 = "hello"
s2 = 'world'
s3 = """this is
a multiline string"""
````

* Use **double**, **single**, or **triple** quotes.
* Triple quotes are used for **multi-line strings** or **docstrings**.

---

## 🔹 2. Indexing

Each character in a string has an index (position):

```python
s = "sunflower"
print(s[0])    # 's'
print(s[3])    # 'f'
print(s[-1])   # 'r' (last character)
```

* Python uses **0-based indexing**.
* Negative indexes access characters from the **end**.

---

## 🔹 3. Slicing

You can extract portions of a string:

```python
s = "sunflower"
print(s[0:3])   # 'sun'
print(s[:5])    # 'sunfl'
print(s[3:])    # 'flower'
print(s[::-1])  # 'rewolfnus' (reversed)
```

---

## 🔹 4. String Methods

```python
name = "Bhavya Tripathy"

print(name.upper())        # 'BHAVYA TRIPATHY'
print(name.lower())        # 'bhavya tripathy'
print(name.find("T"))      # 7
print(name.replace("Tripathy", "T."))  # 'Bhavya T.'
```

| Method         | Description                    |
| -------------- | ------------------------------ |
| `upper()`      | Convert to uppercase           |
| `lower()`      | Convert to lowercase           |
| `find(sub)`    | First index of substring       |
| `replace(a,b)` | Replace all `a` with `b`       |
| `strip()`      | Remove leading/trailing spaces |
| `split()`      | Convert string to list         |
| `join()`       | Join list into string          |

---

## 🔹 5. Immutability

Strings are **immutable** in Python. You can't change characters in-place:

```python
s = "hello"
s[0] = "H"  # ❌ Error!
```

To "modify" a string, create a new one.

---

## 🔹 6. String Formatting

Modern and powerful way to insert variables into strings:

```python
name = "Bhavya"
print(f"Hello, {name}!")  # Hello, Bhavya!
```

---

## 🔹 7. Looping Through a String

```python
for ch in "sunflower":
    print(ch)
```

---

## 🔹 8. Palindrome Checker

A **palindrome** reads the same forwards and backwards:

```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
```

---

