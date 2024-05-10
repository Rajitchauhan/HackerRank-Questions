from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj):
        # code here
        queue = deque()
        visited = set()
        queue.append(0)
        visited.add(0)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for child in adj[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
                    
        return res
    
    
#driver code

if  __name__ == "__main__":
    T = int(input('enter the number of test cases'))
    for i in range(T):
        V  ,E = map(int , input(' enter V and E (i.e. 5 4)').split())
        adj = [[] for i in range(V)]
        print(f'adj before :: {adj}')
        for _ in range(E):
            u  ,v = map(int , input('enter vartex u to v (i.e. (0 , 2))').split())
            adj[u].append(v)
        print(f'adj after :: {adj}')
        
        ob = Solution()
        
        ans = ob.bfsOfGraph(V  , adj)
        
        for i in range(len(ans)):
            print(ans[i] , end=" ")
        print()

# from collections import deque
# import sys

# class Solution:
#     def bfsOfGraph(self, V: int, adj):
#         queue = deque()
#         visited = set()
#         queue.append(0)
#         visited.add(0)
#         res = []

#         while queue:
#             node = queue.popleft()
#             res.append(node)

#             for child in adj[node]:
#                 if child not in visited:
#                     queue.append(child)
#                     visited.add(child)

#         return res

# # Driver code
# if __name__ == "__main__":
#     T = int(sys.stdin.readline().strip())
    
#     for _ in range(T):
#         V, E = map(int, sys.stdin.readline().strip().split())
#         adj = [[] for _ in range(V)]
        
#         for _ in range(E):
#             u, v = map(int, sys.stdin.readline().strip().split())
#             adj[u].append(v)

#         ob = Solution()
#         ans = ob.bfsOfGraph(V, adj)

#         for i in range(len(ans)):
#             print(ans[i], end=" ")
#         print()
