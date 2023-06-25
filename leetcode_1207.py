def uniqueOccurrences(arr):
    countarr = []
    for element in arr:
        count = 0
        for index, element2 in enumerate(arr):
            if element2 == element:
                count += 1
                arr[index] = None
        print(count,'count',element)
        if count in countarr and element is not None:
            return 'false'
        if element is not None and count != 0:
            countarr.append(count)
    return 'true'
arr=[6,6,-1]
print(uniqueOccurrences(arr))