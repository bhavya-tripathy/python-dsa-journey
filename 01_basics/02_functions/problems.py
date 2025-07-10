
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
