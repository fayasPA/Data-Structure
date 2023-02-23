# arr = [64, 25, 12, 22, 11,25]
# arr = [1,3,2,4,5]
arr = [8,3,2,12,5,6]
# for i in range(len(arr)):
#     min = i
#     for j in range(i+1,len(arr)):
#         if arr[min] > arr[j]:
            # temp = arr[min]
            # arr[min] = arr[j]
            # arr[j] = temp
# print("Sorted Array:")
# print(arr)

# Bubble Sort
# for i in range(len(arr)):
#     swapped = False
#     for j in range(len(arr)-1):
#         if arr[j] > arr[j+1]:
#             swapped = True
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#     if not swapped:
#         break
# print(arr)

# Insertion Sort
print(arr)
for i in range(len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
print(arr)
mid=len(arr)//2
