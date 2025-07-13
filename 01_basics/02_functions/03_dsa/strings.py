#strings.py
#A walkthrough of core string concepts in python

# 🔹 1. String creation
s1 = "hello"
s2 = 'world'
s3 = """This is
a multiline string"""

print(s1, s2, s3)

# 🔹 2. Indexing
print("First character of s1:", s1[0])
print("Last character of s2:", s2[-1])

# 🔹 3. Slicing
s = "sunflower"
print("First 3 characters:", s[0:3])     # sun
print("From start to 5:", s[:5])         # sunfl
print("From 3 to end:", s[3:])           # flower
print("Reversed string:", s[::-1])       # rewolfnus

# 🔹 4. String methods
name = "Bhavya Tripathy"
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Find 'T':", name.find('T'))
print("Replace 'Tripathy' with 'T.':", name.replace("Tripathy", "T."))
print("Split by space:", name.split())
print("Join with hyphen:", "-".join(name.split()))

# 🔹 5. Immutability
try:
    name[0] = 'b'  # This will raise an error
except TypeError as e:
    print("Error:", e)

# 🔹 6. String formatting
user = "Bhavya"
print("Hello, {}".format(user))  # Using format method
print(f"Hello, {user}")  # Using f-string (Python 3.6+)

# 🔹 7. Looping through a string
word = "sunflower"
print("Characters in 'sunflower':")
for cahr in word:
    print(cahr, end = " ")  # Corrected typo in print function
print() # Newline after loop

# 🔹 8. Palindrome checker
def is_palindrome(s):
   return s == s[::-1]

test1 = "radar"
test2 = "hello"
print(f"Is '{test1}' a palindrome?", is_palindrome(test1))
print(f"Is '{test2}' a palindrome?", is_palindrome(test2))

# 🔹 9. BONUS: Vowel counter
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

print("Vowels in 'sunflower':", count_vowels("sunflower"))