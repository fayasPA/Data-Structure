# class Node:
#     def __init__(self,key) -> None:
#         self.key = key
#         self.lchild = None
#         self.rchild = None

class BinarySearchTree:
    def __init__(self,key=None) -> None:
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:            #Ignoring duplicate value
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BinarySearchTree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BinarySearchTree(data)
    def search(self,data):
        if self.key == data:
            print("data found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Not Found")                
        if data > self.key:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Not Found")                
    # pre-order traversal
    def pre_order(self):
        if self.key:
            print(self.key,end="-->")
            if self.lchild:
                self.lchild.pre_order()
            if self.rchild:
                self.rchild.pre_order()
        else:
            print("Tree is empty")        
    # in-order traversal
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key,end="-->")
        # else:
        #     print("Tree is empty")
        if self.rchild:
            self.rchild.in_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key,end='-->')

    def delete(self,data,root_val):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,root_val)
            else:
                print('Given NO is Not present in the tree')
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,root_val)
            else:
                print("Given No is not present in the tree")
        else:                       #else case for data == self.key
            # Below 3 if conditions will checked if node to be
            # deleted has zero or 1 child
            if self.lchild is None and self.rchild is None:
                self.key = None
                return
            elif self.lchild is None: 
                temp = self.rchild
                if data == root_val:            # condition for root value with only one child
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            elif self.rchild is None:
                temp = self.lchild
                if data == root_val:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            # Below condition is if Node to be delted has two childs
            # There are two options for this:
            # 1.replace Node to be deleted with left tree's highest key
            # 2.replace with right tree's smallest value 
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,root_val)
        return self
def count(node):
        if node is None:
            return 0
        return 1 + count(node.lchild) + count(node.rchild)


root = BinarySearchTree(10)
# list1 = [20,41,54,14,78,2]
list1 = [6,3,1,6,98,3,7]
# list1 = [11,12]
for i in list1:
    root.insert(i)
root.search(7)
# root.pre_order()
print('\nIn-Order',end='-->')
root.in_order()
root.delete(6,root.key)
print('\nIn-Order After deletion',end='-->')
root.in_order()
# print('\nPost-Order',end='-->')
# root.post_order()

# print('fdshfdksf',count(root))