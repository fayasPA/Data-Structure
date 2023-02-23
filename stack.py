# stack = []
# def push():
#     stack.append(input("Enter the element\n"))
#     print(stack)
# def pop_element():
#     if not stack:
#         print("stack is empty\n")
#     else:
#         stack.pop()
#         print(stack)

# while True:
#     choice = int(input('Enter any choice \n 1.push \n 2.pop \n 3.quit \n'))
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop_element()
#     elif choice == 3:
#         break
#     else:
#         print("INVALID CHOICE")

# import collections
# stack = collections.deque()
# print(stack)
# stack.append(10)
# stack.append(25)
# stack.append(16)
# stack.append(19)
# print(stack)
# stack.pop()
# print(stack[-1])

# s = [0] * 5
# print(s)
# s.insert(0,25)
# print(s)

class stack_array:
    def __init__(self,size=3):
        self.stack = [None]*size
        self.size = size
    def push(self):
        val = int(input('Enter a value'))
        if self.stack[0] is None:
            self.stack[0] = val
        else:
            i = 0
            while self.stack[i] is not None:
                i += 1
            self.stack[i] = val
    def pop(self):
        if self.stack[0] is None:
            print('stack is empty')
        else:
            i = 0
            while self.stack[i] is not None:
                i += 1
            self.stack[i-1] = None
    def print_stack(self):
        if self.stack is None:
            print('stack is empty')
        else:
            i = 0
            while self.stack[i] is not None:
                i += 1
            print(self.stack[0:i])
s = stack_array(5)
while True:
    choice = int(input('Enter any choice \n 1.push \n 2.pop \n 3.quit \n'))
    if choice == 1:
        s.push()
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.print_stack()
        break
    else:
        print("INVALID CHOICE")