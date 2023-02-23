# class Node:
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next

# class linkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_start(self,data):
#         node = Node(data,self.head)
#         self.head = node

#     def print(self):
#         if self.head is None:
#             print("linked empty")
#             return

#         itr = self.head
#         listr = ''

#         while itr:
#             listr += str(itr.data) + '-->'
#             itr = itr.next

#         print(listr)

#     def insert_at_end

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head == None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data, '-->', end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print('Node not found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("Linked list is empty")
        else:
            if x == self.head.data:
                self.head = self.head.ref
            else:
                n = self.head
                while n.ref is not None:
                    if n.ref.data == x:
                        break
                    n = n.ref
                if n is None:
                    print("Node Not Found")
                else:
                    n.ref = n.ref.ref

    def rev_sll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            self.head = None
            while n is not None:
                nxt = n.ref
                n.ref = self.head
                self.head = n
                n = nxt

    def count_node(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            count = 0
            n = self.head
            while n is not None:
                n = n.ref
                count += 1
            return count


ll1 = LinkedList()
ll1.add_begin(10)
ll1.add_end(5)
ll1.add_after(500, 5)
ll1.add_before(2500, 10)
# ll1.rev_sll()
# ll1.delete_begin()
# ll1.delete_end()
# ll1.delete_by_value(xx5)
ll1.print_LL()
# print("\ncount=",ll1.count_node())


class N:
    def __init__(self, data) -> None:
        self.pref = None
        self.data = data
        self.nref = None
