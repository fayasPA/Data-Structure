# def duplicate(arr):
#     for i in range(len(arr)):
#         count = 0
#         for j in range(i,len(arr)):
#             if arr[i] == arr[j]:
#                 count += 1
#                 arr[j] = 0
#         if count > 1:
#             print(arr[i])
        
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ll:
    def __init__(self):
        self.head = None
    
    def addbegin(self,data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def printll(self):
        n = self.head
        while n is not None:
            print(n.data,end=" ")
            n = n.next
    
    def printalt(self):
        n = self.head
        count = 0
        while n.next is not None:
            count += 1
            # if (count % 2) != 0:
            print(n.data,end="-->")
            n =n.next.next


ll1 = ll()
ll1.addbegin(5)
ll1.addbegin(10)
ll1.addbegin(25)
ll1.addbegin(35)
ll1.addbegin(50)
ll1.printll()
ll1.printalt()