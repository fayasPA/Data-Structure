class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.graph = []
        self.node_count = 0
    def add_nodes(self,v):
        if v in self.nodes:
            print("Node is already present")
        else:
            self.node_count = self.node_count + 1
            self.nodes.append(v)
            for n in self.graph:
                n.append(0)
            temp = [0] * self.node_count
            # for i in range(self.node_count):
            #     temp.append(0)
            self.graph.append(temp)
    def print_graph(self):
        for i in range(self.node_count):
            for j in range(self.node_count):
                print(self.graph[i][j],end=' ')
            print()
        print('Node_count',self.node_count)

    def add_edge(self,v1,v2):
        # adding an edge to undirected and un-weighted graph
        if v1 not in self.nodes or v2 not in self.nodes:
            print("Given node is not present")
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)
            self.graph[index1][index2] = 1
            self.graph[index2][index1] = 1

    def add_edge_with_weight(self,v1,v2,weight):
        # adding an edge to DIRECTED and WEIGHTED graph
        if v1 not in self.nodes or v2 not in self.nodes:
            print("Given node is not present")
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)
            self.graph[index1][index2] = weight

    def delete_node(self,v):
        if v not in self.nodes:
            print('Node is not present in Graph')
        else:
            index1 = self.nodes.index(v)
            self.node_count = self.node_count - 1
            self.nodes.remove(v)
            self.graph.pop(index1)
            for idx in self.graph:
                idx.pop(index1)
            
    def delete_edge(self,v1, v2):
        if v1 not in self.nodes and v2 not in self.nodes:
            print('Vertex is not present in Graph')
        else:
            idx1 = self.nodes.index(v1)
            idx2 = self.nodes.index(v2)
            self.graph[idx1][idx2] = 0
            self.graph[idx2][idx1] = 0


# g = Graph()
# g.add_nodes('A')
# g.add_nodes('B')
# g.add_nodes('C')
# g.add_edge('A','B')
# g.add_edge_with_weight('A','C',25)
# # g.delete_node('B')
# g.delete_edge('C','A')
# g.print_graph()




# Adjacency list
class Graph_adj_list:
    def __init__(self) -> None:
        self.graph = {}
        self.node_count = 0
        # self.visited = set()
    def add_nodes(self,v):
        if v in self.graph:
            print("Node is already present")
        else:
            self.graph[v] = []

    def print_graph(self):
        print(self.graph)

    def add_edge(self, v1, v2):
        if v1 not in self.graph.keys() or v2 not in self.graph.keys():
            print("Given node is not present")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def add_edge_with_weight(self, v1, v2, weight):
        # Here we are adding edge for directed weight graph

        if v1 not in self.graph.keys() or v2 not in self.graph.keys():
            print('Given Node is not present in the Graph')
        else:
            # list1 = [v2, weight]
            self.graph[v1].append([v2, weight])

    def delete_node(self,v):
        if v not in self.graph:
            print('Node/vertex is not present in Graph')
        else:
            self.graph.pop(v)
            for idx in self.graph:
                list1 = self.graph[idx]
                if v in list1:
                    list1.remove(v)

    def delete_node_with_weight(self,v):
        if v not in self.graph:
            print("given node is not present in the Graph")
        else:
            self.graph.pop(v)
            for i in self.graph:
                list1 = self.graph[i]
                for j in list1:
                    if v in j:
                        list1.remove(j)
                        break

    def delete_edge(self, v1, v2):
        # for un-weighted graph

        if v1 not in self.graph and v2 not in self.graph:
            print("Given node is not present in the Graph")
        # else:
        #     if v2 in self.graph[v1]:
    
    def DFS(self, node, visited,):
        if node not in self.graph:
            print("Node is not present in graph")
        if node not in visited:
            print(node)
            visited.add(node)
            for i in self.graph[node]:
                self.DFS(i,visited)

    def BFS(self, node):
        visited = set()
        if node not in self.graph:
            print("The node not in self.graph")
            return
        queue = []
        queue.append(node)
        while queue:
            current = queue.pop(0)
            if current not in visited:
                print(current,"-->",end=" ")
                visited.add(current) 
                for i in self.graph[current]:
                    queue.append(i)

adj_list = Graph_adj_list()
adj_list.add_nodes('A')
adj_list.add_nodes('B')
adj_list.add_nodes('C')
adj_list.add_nodes('E')
adj_list.add_nodes('D')
adj_list.add_edge('A', 'C')
adj_list.add_edge('A', 'E')
adj_list.add_edge('C', 'D')
# adj_list.add_edge_with_weight('B','A',1254)
# adj_list.delete_node_with_weight('A')
adj_list.print_graph()
adj_list.DFS('A',visited=set())
print("BFS")
adj_list.BFS('A')
