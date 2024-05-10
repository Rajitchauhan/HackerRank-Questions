# graph represent using matrix

class Graph:
    def __init__(self , size) -> None:
        self.graph = []
        
        for i in range(size):
            self.graph.append([0 for j in range(size)])
            
        self.Size = size
        
    def addEdges(self , v1 , v2):
        if(v1 == v2):
            print(f'v1 and v2 are same vertice {v1} :: {v2} ')
        self.graph[v1][v2] = 1
        self.graph[v2][v1] = 1
        
    def remove(self , v1 , v2):
        if self.graph[v1][v2] == 0:
            print("no  edges are present")
            return
        self.graph[v1][v2] = 0
        self.graph[v2][v1] = 0
        
    def printMatrix(self):
        for row  in self.graph:
            for val  in row:
                print('{:4}'.format(val))
            print()
                
                
                
G = Graph(4)
# print(G.graph)   

G.printMatrix()          

      
      
      
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def remove_edge(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

    def print_graph(self):
        for row in self.adj_matrix:
            print(row)

# Example usage:
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.print_graph()

# Remove edge between vertices 0 and 2
g.remove_edge(0, 2)

print("\nAfter removing edge:\n")
g.print_graph()
      
        