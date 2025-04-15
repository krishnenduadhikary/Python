#Questio Answered:-------

#1
p=10
q=p
r=10
print(id(p),id(q),id(r))
#2
print("General"+"Knowledge")
print("General"*2)
#4
a,b=5,2
c=a/b
d=a//b
e=a%b
f=a%3.0
g=6.0%4
print(a,b,c,d,e,f,g)
#6
x=28/4 or 3.0+2*3
print(x)
#10
#x**y
#11
print(14+13%15)
#12
A=16
B=15
print(A%B//A)
#13
x=int(13.25+4/2)
print(x)
print(8/4/2)
#19
for i in range(-1,7,-2):
    for j in range(3):
        print(i,j)

#19
for i in range(1,3,1):
    for j in range(i+1):
        print("*")

#20
for name in ['Sanjoy','Tarun','Aparna','Hiya']:
    print(name)
    if name[0]=='A':
        break
    else:
        print('Finished!')
print('Got it')
#