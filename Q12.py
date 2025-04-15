#Check if the number is divisible by 5 and 11
def divisible(number):
    if number % 5 == 0 and number % 11 == 0:
        return True
    else:
        return False

number = int(input("Enter a number: "))
 
if divisible(number):
    print(f"{number} is divisible by both 5 and 11.")
else:
    print(f"{number} is not divisible by both 5 and 11.")
