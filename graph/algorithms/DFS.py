class Solution:
    def DFSUtil(self  , V , adj , node , res , visited):
        res.append(node)
        visited.add(node)
        
        for neibhour in adj[node]:
            if neibhour  not in visited:
                self.DFSUtil(V , adj , neibhour , res , visited)
        return res
        
    def DFS(self , V ,  adj):
        node = 0
        res = []
        visited = set()
        return self.DFSUtil(V , adj , node , res , visited)
    
    
    
if __name__ == '__main__':
    T = int(input('enter no of test case'))
    for _ in range(T):
        V , E = map(int  , input('enter vartex and Edges (i.e. 5 4)').split())
        
        adj = [[] for i in range(V)]
        
        for i in range(E):
            u , v = map(int , input('enter the u and v (i.e. 0 , 2)').split())
            adj[u].append(v)
            
        obj = Solution()
        ans = obj.DFS(V , adj)
        
        # print(obj.DFS)
        for i in range(len(ans)):
            print(ans[i] , end= ' ')
        