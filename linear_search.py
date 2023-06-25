# arr =[10, 20, 80, 30, 60, 50,110, 100, 130, 170]
# search = 100
# counter = 1
# for i in arr:
#     if search == i:
#         flag = 1
#         break
#     counter += 1
# if flag == 1:
#     print(search," elment found at pos ",counter)
# else:
#     print(search," elment not found")

arr =[10, 20, 30, 50, 60, 80, 100, 110, 130, 170]
f = 0
l = len(arr)
search = 60
flag = 0
for i in range(l):
    m = int((f + l)/2)
    if search == arr[m]:
        flag = 1
        pos = m
        break
    elif search > arr[i]:
        f = i+1
    elif search < arr[i]:
        l = i-1
if flag == 1:
    print("'",search,"'"," elment found at pos ",pos+1)
else:
    print(search," elment not found")

