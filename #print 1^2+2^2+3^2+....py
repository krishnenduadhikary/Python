#print 1^2+2^2+3^2+.....+n^2
n=int(input("Enter an integer:"))
sum=0
for i in range(1,n+1):
    term=i*i
    sum+=term
    i+=1
print("Result=",sum)