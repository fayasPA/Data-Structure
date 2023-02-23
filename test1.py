
def search(node,data):
        if node.key == data:
            return True
        if data > node.key:
                if node.right:
                    search(node.right,data)
                else:
                    return False
        if data < node.key:
            if node.left:
                search(node.left,data)
            else:
                 return False
search(root_node,search_item)


def DFS(x,graph):
     visited = set()
     stack = []
     stack.append(x)
     while stack:
          current = stack.pop()
          visited.add(current)
          for i in graph[current]:
               stack.append(i)
               

DFS('A',{'A':['B','C'],'B':})
