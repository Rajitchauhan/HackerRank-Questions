from collections import deque
class Solution:

    def isValid(self , i , j , grid , vis , n , m , count):
        if(i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0):
            count[0] += 1
            return False
        else:
            if vis[i][j] ==1:
                return False
            return  True
    
    def bfs(self , i , j , grid , vis , count):
        peri = 0
        queue = deque()
        n , m = len(grid) , len(grid[0])
        queue.append([i , j])
        vis[i][j] = 1
        while queue:
            r , c  = queue.popleft()
            

            dire = [[r+1 , c] , [r , c+1] , [r-1 , c] , [r , c-1]]

            for i , j in dire:
                if self.isValid(i , j , grid , vis , n , m , count):
                        
                    queue.append([i , j ])
                    vis[i][j] = 1
        return count[0]
    def islandPerimeter(self, grid) -> int:
        # peri = 0
        # queue = deque()
        count = [0]
        n , m = len(grid) , len(grid[0])
        vis = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return self.bfs(i , j , grid , vis , count)
                    
        
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4
 

# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid