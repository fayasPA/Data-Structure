s = []
res = 0
# b = [[1,1,1,0,0,0], [0,1,0,0,0,0], [1,1,1,0,0,0],[0,0,2,4,4,0], [0,0,0,2,0,0], [0,0,1,2,4,0]]
# for i in range(6-2):
#     s = []
#     for j in range(6-2):
#         sum = 0
#         for k in range(j,j+3):
#             sum = sum + b[i][k]
#         count = 1
#         for l in range(i+1,i+3):
#             mcount = 1
#             for m in range(j,j+3):
#                 if count == 1 and mcount != 2 :
#                     mcount += 1
#                     pass
#                 else:
#                     mcount += 1
#                     sum = sum + b[l][m]
#             count += 1
#         s.append(sum)
#         if res < sum:
#             res = sum
    # res.append(s)
# print(res)


b = [[0,-4,-6,0,-7,-6], [-1,-2,-6,-8,-3,-1], [-8,-4,-2,-8,-8,-6],[-3,-1,-2,-5,-7,-4], [-3,-5,-3,-6,-6,-6], [-3,-6,0,-8,-6,-7]]
for i in range(6-2):
    for j in range(6-2):
        sum = b[i][j] + b[i][j+1] + b[i][j+2] + b[i+1][j+1] + b[i+2][j] + b[i+2][j+1] + b[i+2][j+2] 
        if res < abs(sum):
            res = sum
print(res)