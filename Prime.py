#write a python program to check a number is prime number or not

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get user input for the number to check
num = int(input("Enter a number: "))

# Check if the number is a prime number
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
