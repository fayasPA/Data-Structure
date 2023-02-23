class Node:
    def __init__(self,data):
        self.pref = None
        self.data = data
        self.nref = None

class D_linked_list:
    def __init__(self):
        self.head = None
    
    def print_dll(self):
        n = self.head
        if self.head is None:
            print("Linked lIst is empty")
        else:
            n = self.head
            print("Linked list in order")
            while n is not None:
                print(n.data,"-->",end=' ')
                n = n.nref
            
    def print_dll_reverse(self):
        if self.head is None:
            print("Linked lIst is empty")
        else:
            print("Linked list in reverse order")
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,'-->',end=' ')
                n = n.pref

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.nref
            self.head.pref = None

dl1 = D_linked_list()
dl1.add_begin(100)
dl1.add_end(200)
dl1.add_end(300)
dl1.add_begin(5000)
# dl1.delete_begin()
# dl1.print_dll()
dl1.print_dll_reverse()