#write a python program to display the first n terms of fibonacci series
def fibonacci(n):
    if n <= 0:
        return []

    fib_series = [0, 1]

    for _ in range(2, n):
        fib_series += [fib_series[-1] + fib_series[-2]]

    return fib_series

# Get user input for the number of terms
n = int(input("Enter the number of terms for Fibonacci series: "))

# Display the first n terms of Fibonacci series
result = fibonacci(n)
print(f"The first {n} terms of the Fibonacci series are: {result}")
