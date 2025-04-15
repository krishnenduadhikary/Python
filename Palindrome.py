#write a python program to  check a number is palindrome or not
def is_palindrome(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    return original_num == reversed_num

# Get user input for the number to check
user_input = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")


