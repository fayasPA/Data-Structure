class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def contains(self, data):
        if self.root is None:
            return False
        else:
            return self._contains(data, self.root)

    def _contains(self, data, node):
        if data == node.data:
            return True
        elif data < node.data and node.left is not None:
            return self._contains(data, node.left)
        elif data > node.data and node.right is not None:
            return self._contains(data, node.right)
        else:
            return False

    def delete(self, data):
        if self.root is not None:
            self.root = self._delete(data, self.root)

    def _delete(self, data, node):
        if data == node.data:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                parent = node
                successor = node.right
                while successor.left:               #for finding the right child's smallest key/data
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
                return node
        elif data < node.data and node.left is not None:
            node.left = self._delete(data, node.left)
            return node
        elif data > node.data and node.right is not None:
            node.right = self._delete(data, node.right)
            return node
        else:
            return node

    def preorder(self):
        if self.root is not None:
            self._preorder(self.root)

    def _preorder(self, node):
        print(node.data, end=" ")
        if node.left is not None:
            self._preorder(node.left)
        if node.right is not None:
            self._preorder(node.right)

    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)

    def _inorder(self, node):
        if node.left is not None:
            self._inorder(node.left)
        print(node.data, end=" ")
        if node.right is not None:
            self._inorder(node.right)

    def postorder(self):
        if self.root is not None:
            self._postorder(self.root)

    def _postorder(self, node):
        if node.left is not None:
            self._postorder(node.left)
        if node.right is not None:
            self._postorder(node.right)
        print(node.data, end=" ")

root = BinarySearchTree()
# list1 = [20,41,54,14,78,2]
# list1 = [6,3,1,6,98,3,7]
list1 = [10,12]
for i in list1:
    root.insert(i)
# root.search(55)
# # root.pre_order()
print('\nIn-Order',end='-->')
root.inorder()
root.delete(10)
print('\nIn-Order',end='-->')
root.inorder()