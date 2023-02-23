# class hashtable:
#     def __init__(self,size) -> None:
#         self.size = size
#         self.arr = [None] * size
#     def hash(self,key):
#         return key % self.size
#     def put(self,key,val):
#         k = hash(key)
#         self.arr[k] = val
#     def get(self,key):
#         k = hash(key)
#         if self.arr[k] is not None:
#             print(self.arr[k])
#         else:
#             print("not found")
# h = hashtable(10)
# h.put(4,'fayas')
# h.get(4)

# arr = [1,45,25,48,7,6]

# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]

# print(arr)

def sort(arr,low,high):
    if low>=high:
        return
    s = low
    e = high
    m = int(s + (e-s)/2)
    pivot = arr[m]
    while s<=e:
        while arr[s] < pivot:
            s += 1
        while arr[e] > pivot:
            e -= 1
        if s<=e:
            arr[s],arr[e] = arr[e],arr[s]
            s += 1
            e -= 1
    sort(arr,low,e)
    sort(arr,s,high)

arr = [1,2,48,5,74,3]
sort(arr,0,len(arr)-1)
print(arr)