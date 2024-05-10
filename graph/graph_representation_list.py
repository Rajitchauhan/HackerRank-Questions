# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.adj_list = defaultdict(list)

#     def add_edge(self, u, v):
#         self.adj_list[u].append(v)
#         self.adj_list[v].append(u)
    
#     def print_graph(self):
#         for vertex, neighbors in self.adj_list.items():
#             print(f"{vertex} -> {neighbors}")

# # Example usage:
# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.print_graph()

# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.adj_list = defaultdict(list)

#     def add_edge(self, u, v):
#         self.adj_list[u].append(v)
#         self.adj_list[v].append(u)

#     def remove_edge(self, u, v):
#         self.adj_list[u].remove(v)
#         self.adj_list[v].remove(u)

#     def print_graph(self):
#         for vertex, neighbors in self.adj_list.items():
#             print(f"{vertex} -> {neighbors}")

# # Example usage:
# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 3)

# g.print_graph()

# # Remove edge between vertices 0 and 2
# g.remove_edge(0, 2)

# print("\nAfter removing edge:\n")
# g.print_graph()
from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        
    def add_edge(self , u  , v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def printGraph(self):
        for vertices ,  neighbour in self.graph.items():
            print(f'{vertices} -> {neighbour}')
            
    def removeEdges(self  , u , v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)
        
g = Graph() 
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.printGraph()
