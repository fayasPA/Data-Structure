'''
Given an integer array nums sorted in non-decreasing order,
 remove the duplicates in-place such that each unique element appears only once.
 The relative order of the elements should be kept the same.
 Then return the number of unique elements in nums.
'''

def removeDuplicates(nums):
    j = 0
    for i in range(len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return nums

print(removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,3,4]))