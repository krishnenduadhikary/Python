#print 1!+2!+3!+....+n!
n=int(input("Enter an integer:"))
fact=1
sum=0
for i in range(1,n+1):
    fact*=i
    sum+=fact
    i+=1
print("Result=",sum)