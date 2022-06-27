# students_age = [12, 34, 5, 3, 2, 4, 45]


# students_age[2] = 56
# for age in students_age:
#     print(age)

num = input("Enter number :")
num = int(num)

f = list(range(0, num))

j = 0

for i in f:
    if j > 1:
        f[j] = f[j-1] + f[j-2]
    j = j + 1

print(f)

