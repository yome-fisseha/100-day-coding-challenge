a=input("enter first number")
b=input("enter second number")

a=int(a)
b=int(b)

if a<b :
    min=a
    max=b
else :
    min=b
    max=a

i=1
lcm = 0

while(lcm == 0):
    n=i*min
    i = i + 1
    if n % max == 0:
        lcm = n

print(lcm)


    


