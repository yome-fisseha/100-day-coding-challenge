from re import I


a=input("enter number")
a=int(a)

i=0
j=1
dontstop=True
while (dontstop ) :
    n=i+j
    i=j
    j=n
    if a==n:
        print("it is fibonacci number")
        dontstop=False
    elif a < n:
        print("it is not fibonacci number")
        dontstop=False
