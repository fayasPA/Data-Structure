
# def rotate(a=[],i=0,num = 0,first = 0):

#     if i == len(a)-1 and num != 0:
#         a[len(a)-1] = first
#         num -= 1
#         if i == len(a)-1 and num == 0:
#             return print(a)
#         i = 0
#         first = a[0]     
#     a[i] = a[i+1]

#     rotate(a,i=i+1,num=num,first=first)

# a=[1,2,3,4,5]
# rotate(a,first = a[0],num = 10)



# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")
# t = tuple(zip(zip(range(5)),range(len('abc'))))
# print(t)
# print(tuple(zip(a)))







# a = [1,2,3,4,5]
# num = 2
# first = a[0]
# for i in range(0,len(a)):
#     if i == len(a)-1 and num != 0:
#         a[len(a)-1] = first
#         i = 0
#         num -= 1
#         print(a)
#         first = a[0]
#         print(i)
#     print(i)
#     a[i] = a[i+1]

# s = []
# s.append(10)
# s.append(10)
# s.append(20)
# print(s)
# s.append(20)

# s = 'His expression went dark.'
# print(s.split('.'))
sd = {'c':{'d':{'e':4565}}}
# sd = [0]*5
sd['a'] = 54
sd['b'] = 355
# sd.append(['a',254])
# sd[5].append(14587)
sd.pop('a')
print(sd)
# print('yygyjug',sd.get('c'))