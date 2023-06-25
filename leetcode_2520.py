a = 1248
print(a%(a%10))
a1 = a
count = 0
while a1 > 0:
    if (a % (a1%10)) == 0:
        count += 1
    a1 = a1 // 10
print(count)