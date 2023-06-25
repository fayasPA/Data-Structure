a = [1,4,10,25,78]
val = 25
s = 0
e = len(a) - 1
flag = 0
while s<e:
    m = (e + s) // 2
    if a[m] == val:
        flag = 1
        break
    elif val > a[m]:
        s = m+1
    else:
        e = m-1
    
if flag == 1:
    print("True")
else:
    print("false")

for i in a:
    if(i<10):
        del(i)
print(a)