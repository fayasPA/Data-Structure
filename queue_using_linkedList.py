class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue_ll:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            self.front = self.front.next
    def print_ll(self):
        if self.front is None:
            print("Queue is empty")
        else:
            n = self.front
            while n is not None:
                print(n.data,end="-->")
                n = n.next
q = queue_ll()
q.enqueue(5)
q.enqueue(20)
q.enqueue(15)
q.enqueue(45)
q.print_ll()
print()
q.dequeue()
q.dequeue()
q.print_ll()