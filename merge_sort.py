import random
arr = [random.randint(0,100) for _ in range(10)]

# MERGE SORT
print(arr)
def merge(first,second):
    mix = []
    i = j = 0 
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            mix.append(first[i])
            i += 1
        else:
            mix.append(second[j])
            j += 1
    # if first or second is not finished
    while i < len(first):
        mix.append(first[i])
        i += 1
    while j < len(second):
        mix.append(second[j])
        j += 1
    return mix
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)
print(mergeSort(arr))
