#write a python program to find LCM of two numbers
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def find_lcm(x, y):
    gcd = find_gcd(x, y)
    lcm = (x * y) // gcd
    return lcm

# Get user input for the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and display the LCM
lcm_result = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm_result}")
