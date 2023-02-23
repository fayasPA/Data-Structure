class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    def pop(self):
        if self.top is None:
            print("stack is empty")
        else:
            self.top = self.top.next
    def print_s(self):
        n = self.top
        while n is not None:
            print(n.data,end=' ')
            n = n.next
    def middle(self):
        if self.top is None:
            print("stack is empty")
        else:
            fast = self.top
            slow = self.top
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow.data
s = stack()
s.push(5)
s.push(55)
s.push(487)
s.push(85)
s.push(174)
s.push(878)
s.pop()
s.print_s()
print()
# print(s.middle())