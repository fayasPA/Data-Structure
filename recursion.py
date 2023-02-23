# def printf(n):
#     a=5
#     if n == 5:
#         print(n)
#         return
#     print(n)
#     printf(n + 1)
# printf(1)   #tail recursion

def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

ans = fibo(4)
print(ans)

# def display(n):
#     if n == 1:
#         return n
#     return display(n-1)
# print(display(5))