#write a python program to reverse a number
def reverse(number):
    revnum = 0
    while number > 0:
        digit = number % 10
        revnum = revnum * 10 + digit
        number = number // 10
    return revnum

# Get user input for the number
number = int(input("Enter a number: "))

# Reverse the number and display the result
result = reverse(number)
print(f"The reversed number is: {result}")
