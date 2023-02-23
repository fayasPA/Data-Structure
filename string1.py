# String1 = 'Welcome to the Geeks World'
# print("String with the use of Single Quotes: ")
# print(String1)

# String2 = '''      Geeks
#             For
#             Life'''
# print("\nCreating a multiline String: ")
# print(String2)

s = "fayas"
print(s)
print(s[::2])

# String3 = "{:>10} {:<10} {:<10}".format('fay',"fjdl",'ghidhsf')
# print(String3)

# s1 = "fayas"
# print("".join(reversed(s1)))

def reverse(string):
    string = list(string)
    string.reverse()
    print(string)
    return "".join(string)
print(reverse("Geeksforgeeks"))