arr = [-12,-45,-78,-89,-92,-95,-99]
n = len(arr)
largest = 4
for j in range(largest):
    max = -99
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
            pos = i
    arr[pos] = -99
print(max)