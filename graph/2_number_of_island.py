from collections import deque

class Solution:
    def isValid(self , r , c  , grid , visited , n ,m):
        return (r < n and c < m and r >=0 and c >=0 and visited[r][c] == 0 and grid[r][c] == 1)
    def BFS(self , i , j , grid , visited , n ,m):
        queue = deque()
        queue.append((i , j))
        
        visited[i][j] = 1
        
        while queue:
            row , col = queue.popleft()
            
            lt = [[row , col+1] , [row+1 , col] , [row-1 , col]
            , [row , col-1]
            , [row-1 , col-1] , [row-1 , col+1] , [row+1 , col+1] ,[row+1 , col-1]]
            
            for r , c in lt:
                if self.isValid(r , c  , grid , visited , n ,m):
                    queue.append((r , c))
                    visited[r][c] = 1

    
    def  numIslands(self,grid):
        n , m = len(grid) , len(grid[0])
        
        visited = [[0 for  j in range(m)] for i in range(n)]
        
        count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    count += 1
                    self.BFS(i , j , grid , visited , n , m)
        return count


if __name__ == "__main__":
    T = int(input('enter test case'))
    
    for _ in range(T):
        V = int(input('Vertex :: '))
        adj = []
        
        for i in range(V):
            temp = list(map(int , input('enter row').split()))
            adj.append(temp)
        print(adj)
        
        obj = Solution()
        print(f'ans :: ' , obj.numIslands(adj))
        
    
            
            