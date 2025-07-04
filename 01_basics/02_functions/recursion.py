def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Factorial of 5 is:", factorial(5))
print("Fibonacci(6) is:", fibonacci(6))