#find prime numbers between 1 to 100
print("prime numbers between 1 to 100 is :")
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            continue outerloop:
 print(i)