a=input("enter first number")
b=input("enter second number")

a=int(a)
b=int(b)

af = []

for n in range(1, a):
    if a % n == 0:
        af.append(n)

hcf = 1

for n in range(1, b):
    if b % n == 0:
        for i in af:
            if n == i:
                hcf =n
print(hcf)




