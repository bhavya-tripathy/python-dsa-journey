
# 1. Write a function to check if a number is prime
# 2. Write a function that returns the factorial of a number
# 3. Write a recursive function to calculate the nth Fibonacci number
# 4. Write a function that takes variable number of arguments and returns their sum
# 5. Write a lambda function to double each element in a list
# 6. Write a function that checks if a string is a palindrome

# 1. Prime number check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 2. Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 3. Fibonacci (recursive)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 4. Sum of variable arguments
def sum_all(*args):
    return sum(args)

# 5. Lambda to double a list
double = lambda lst: [x*2 for x in lst]

# 6. Palindrome check
def is_palindrome(s):
    return s == s[::-1]



### 🧠 `problems.py` – Problem Prompts
# 1. Find factorial of a number using recursion
# 2. Print the nth Fibonacci number
# 3. Find the sum of digits of a number using recursion
# 4. Count number of steps to reduce a number to zero
# 5. Reverse a string using recursion
# 6. Print numbers from n to 1 recursively
# 7. Solve Tower of Hanoi for n disks

# 1. Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 2. Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 3. Sum of digits
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

# 4. Steps to reduce to zero (Leetcode pattern)
def steps_to_zero(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 1 + steps_to_zero(n // 2)
    return 1 + steps_to_zero(n - 1)

# 5. Reverse string
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

# 6. Print from n to 1
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)

# 7. Tower of Hanoi
def hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, helper, source, destination)

