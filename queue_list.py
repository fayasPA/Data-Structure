# queue = []

# def enque():
#     queue.append(int(input("Enter any No.")))
#     print(queue)

# def deque():
#     if not queue:
#         print("queue is empty")
#     else:
#         queue.pop(0)
#         print(queue)

# while True:
#     choice = int(input("Enter your choice \n1.insert an element.\n2.remove an element.\n3.quit\n"))
#     if choice == 1:
#         enque()
#     elif choice == 2:
#         deque()
#     elif choice == 3:
#         break
#     else:
#         print("INVALID CHOICE")

# import collections
# q = collections.deque()
# q.append(10)
# q.append(20)
# q.append(30)
# q.append(40)
# print(q)
# q.popleft()
# print(q)


# PRIORITY Queue
# queue = []
# def enque():
#     queue.append(int(input("Enter any No.")))
#     print(queue)

# def deque():
#     if not queue:
#         print("queue is empty")
#     else:
#         for i in range(len(queue)):
#             for j in range(i+1,len(queue)):
#                 if queue[i] > queue[j]:
#                     queue[i], queue[j] = queue[j], queue[i]
#         queue.pop(0)
#         print(queue)

# while True:
#     choice = int(input("Enter your choice \n1.insert an element.\n2.remove an element.\n3.quit\n"))
#     if choice == 1:
#         enque()
#     elif choice == 2:
#         deque()
#     elif choice == 3:
#         break
#     else:
#         print("INVALID CHOICE")

class queue:
    def __init__(self,size=3):
        self.q_array = [None]*size
        self.front = -1
    def enque(self):
        val = int(input("Enter any value"))
        if self.front == -1:
            self.q_array[0] = val
            self.front += 1
        else:
            i = self.front
            while self.q_array[i] is not None:
                i += 1
            self.q_array[i] = val
            print(self.q_array)
    def deque(self):
        if self.front == -1:
            print('Queue is empty')
        else:
            self.q_array[self.front] = None
            self.front += 1
            print(self.q_array) 
    def print_q(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            i = self.front
            while i < len(self.q_array) and self.q_array[i] is not None:
                print(self.q_array[i],end="  ")
                i += 1
            print(self.q_array)
q = queue()
while True:
    choice = int(input("Enter your choice \n1.insert an element.\n2.remove an element.\n3.quit\n"))
    if choice == 1:
        q.enque()
    elif choice == 2:
        q.deque()
    elif choice == 3:
        q.print_q()
        break
    else:
        print("INVALID CHOICE")
