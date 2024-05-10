from collections import defaultdict , deque
class  Solution:
    def bfs(self , node , graph , visited):
        visited.add(node)
        queue = deque()
        queue.append(node)
        while queue:
            node = queue.popleft()
            
            for child  in graph[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
        
                
    def numProvinces(self, adj, V):
        graph = defaultdict(list)
        n = len(adj)
        for i in range(n):
            for j in range(i+1 , n):
                if(adj[i][j] == 1):
                    graph[i].append(j)
                    graph[j].append(i)
        count = 0
        visited = set()
        for i in range(len(graph)):
            if i not in visited:
                count += 1
                self.bfs(i , graph , visited)
        return count
        


if __name__ == '__main__':
    T = int(input('enter no. of test cases'))
    
    for _ in range(T):
        V = int(input('Enter number of edges'))
        adj = []
        
        for i in range(V):
            temp = list(map(int  , input().split()))
            adj.append(temp)
        print(adj)
        obj = Solution()
        print("ans :: " , obj.numProvinces(adj , V))
        