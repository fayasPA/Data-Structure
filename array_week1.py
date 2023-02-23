# b = 15
# c = 0
# # a = 10^15
# a = (5^c)%8
# print(a)

# def PalinArray(arr ,n):
#     # Code here
#     flag = 0
#     for i in range(n):
#         rev = ""
#         no = str(arr[i])
#         for j in range(len(no)-1,-1,-1):
#             rev = rev + str(no[j])
#         if arr[i] == int(rev):
#             flag = 1
#         else:
#             flag=0
#             break
#     if flag == 1:
#         return 1
#     else:
#         return 0
# print(PalinArray([111,222,333,444,555],5))


original_string = "Hello, World!"
subsequence = original_string[7:12]  # Extracts "World"
print(subsequence)