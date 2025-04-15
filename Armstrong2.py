#write a python program to print Armstrong numbers between a given range
def Armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num

def Display(start, end):
    print(f"Armstrong numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if Armstrong(num):
            print(num)

# Get user input for the range
start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

# Print Armstrong numbers in the given range
Display(start_range, end_range)
