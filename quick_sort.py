#  append 1,2,3 into a list without using append
# arr = [1,2,3]
# result = [None]*len(arr)*2
# for i in range(len(arr)*2):
#     result[i] = arr[i % len(arr)]
# print(result)

# arr = [5,74,4,63,8,7,95]
arr = [5,3,2,12,8,6]

def sort(arr,low,hi):
    if low >= hi:
        return
    s = low
    e = hi
    m = int(s + (e-s) / 2)
    pivot = arr[m]
    while s <= e:
        while arr[s] < pivot:
            s+=1
        while arr[e] > pivot:
            e -= 1
        if s <= e:
            arr[s],arr[e] = arr[e],arr[s]
            s += 1
            e -= 1
    sort(arr,low,e)
    sort(arr,s,hi)
print(arr)
sort(arr,0,len(arr)-1)
print(arr)

