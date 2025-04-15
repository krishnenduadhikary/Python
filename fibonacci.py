#print fibonacci seres for n terms
n = int(input("Enter the number of terms for Fibonacci series:"))

a, b = 0, 1

print("Fibonacci series up to", n, "terms:")
print(a, b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c
