a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

if a > b and a > c:
    print("maximum is ",a)
elif b > c:
    print("maximum is ",b)
else:
    print("maximum is ",c)
