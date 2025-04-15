#write a python program to print prime number between a given range
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def Display(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

# Get user input for the range
start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

# Print prime numbers in the given range
Display(start_range, end_range)
