# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class stack:
#     def __init__(self):
#         self.top = None
#     def push(self,data):
#         new_node = Node(data)
#         if self.top == None:
#             self.top = new_node
#         else:
#             new_node.next = self.top
#             self.top = new_node
#     def print_s(self):
#         n = self.top
#         while n is not None:
#             print(n.data,end=' ')
#             n = n.next
#     def middle(self):
#         if self.top is None:
#             print("stack is empty")
#         else:
#             fast = self.top
#             slow = self.top
#             while fast is not None and fast.next is not None:
#                 slow = slow.next
#                 fast = fast.next.next
#             return slow.data
# s = stack()
# s.push(5)
# s.push(55)
# s.push(487)
# s.push(85)
# s.push(85)
# s.push(85)
# s.print_s()
# print()
# print(s.middle())


def card_average(hand):
    return sum(hand) / len(hand)
hand = [2, 3, 4, 7, 8]
avg = card_average(hand)
# avg = sum(hand)/len(hand)
print(int(avg))
if int((hand[0]+hand[len(hand)-1])/2) == int(avg) or hand[int(len(hand)/2)] == int(avg):
    print((hand[0] + hand[-1]) / 2 == avg or hand[len(hand)//2] == avg)
else:
    print('false')