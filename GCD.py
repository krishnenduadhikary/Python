#find GCD of two numbers
def GCD(a, b):
    y = a % b
    if y == 0:
        return b
    else:
        return GCD(b, y)

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("GCD:", GCD(a, b))
