arr = [5,6]
k = 6
def kth_element(arr, k):
    count = 1
    for i in range(1, arr[-1] + k):
        if i not in arr:
            if count == k:
                return i
            count += 1
print(kth_element(arr, k))