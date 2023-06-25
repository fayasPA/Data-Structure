'''
Given an integer array nums, return the most frequent even element.
If there is a tie, return the smallest one. If there is no such element, return -1.
'''

def mostFrequentEven(nums):
    mfe = {}
    for i in nums:
        count = 1
        if i % 2 == 0:
            if i in mfe.keys():
                print(mfe,'inside')
                mfe[i] += 1
                print(mfe,'after')
            else:
                mfe[i] = count
    m = mfe.values()
    print(list(m))
    return -1

nums = [10,22,22,5,5,5,8,8,8,8]
print(nums)
print(mostFrequentEven(nums))