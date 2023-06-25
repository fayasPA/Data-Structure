def strStr(haystack: str, needle: str):
    for index, hay in enumerate(haystack):
        if haystack[index:len(needle)+index] == needle:
            return index
        print(haystack[index:len(needle)+index])
    return -1


s = 'saajan'
print('fayas', s[1:2])


'''
Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
'''
