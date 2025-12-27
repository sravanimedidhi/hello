def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:   # divisible by some number
            return False
    return True

# Example
num = 29
print(num, "is prime?", is_prime(num))





def fibonacci(n):
    fib_series = [0, 1]                 # start the series with the first two numbers
    for i in range(2, n):               # loop from 2 to n-1
        fib_series.append(fib_series[i-1] + fib_series[i-2])  # sum of last two elements
    return fib_series[:n]               # return only first n elements

num = 10
print(f"First {num} Fibonacci numbers:", fibonacci(num))








def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
num = 5
print(f"Factorial of {num} is {factorial(num)}")








def add_numbers(a, b):
    return a + b

# Example
num1 = 10
num2 = 20
sum_result = add_numbers(num1, num2)

print(f"Sum of {num1} and {num2} is {sum_result}")



