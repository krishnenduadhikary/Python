#Factorial of a given number
def Fact(number):
    if number==0 or number==1:
        return 1
    else:
        return number*Fact(number-1)
number=int(input("Enter a number"))
result=Fact(number)
print(f"The Factorial of {number} is {result}")