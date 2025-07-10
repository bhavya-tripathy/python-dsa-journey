
# 1. Write a function to check if a number is prime
# 2. Write a function that returns the factorial of a number
# 3. Write a recursive function to calculate the nth Fibonacci number
# 4. Write a function that takes variable number of arguments and returns their sum
# 5. Write a lambda function to double each element in a list
# 6. Write a function that checks if a string is a palindrome

# 1. Write a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True