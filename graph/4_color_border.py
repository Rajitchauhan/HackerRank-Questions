from collections import deque

class Solution:
    def inside(self, m, n, ro, co):
        return 0 <= ro < m and 0 <= co < n

    def border(self, m, n, ro, co):
        return ro == m - 1 or ro == 0 or co == n - 1 or co == 0

    def colorBorder(self, grid, r0, c0, color):
        ori = grid[r0][c0]
        vis = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        q = deque()
        m, n = len(grid), len(grid[0])
        q.append((r0, c0))
        vis[r0][c0] = 1
        print()
        print(f'starting vis :: {(r0 , c0)} and values:: {grid[r0][c0]}')
        print()
        while q:
            cur = q.popleft()
            r, c = cur[0], cur[1]

            if self.inside(m, n, r, c) and self.border(m, n, r, c):
                grid[r][c] = color
                print(f'inside border and inside colored {(r , c)} :: {grid[r][c]}')
                print()
            directions = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
            for ro, co in directions:
                if self.inside(m, n, ro, co) and vis[ro][co] == 0:
                    # Neighbor in the same connected component
                    if grid[ro][co] == ori:
                        q.append((ro, co))
                        vis[ro][co] = 1
                        print(f'append in Q and  vis {grid[ro][co]} and {(ro , co)}')
                        print()
                    # Neighbor is not in the connected component, so this square is on the boundary edge
                    else:
                        grid[r][c] = color
                        print(f'not a ori but in inside and not vis {grid[r][c]} : {(r , c)}')
                        print()

        return grid

    

if __name__ == "__main__":
    T = int(input('test case'))
    
    for _ in range(T):
        V = int(input('Vertex :: '))
        grid =[]
        
        for i  in range(V):
            temp = list(map(int , input('enter the row').split()))
            grid.append(temp)
        r , c = map(int , input('enter the row and col ::').split())
        color = int(input('enter the  color'))
        obj = Solution()
        print(obj.colorBorder(grid , r , c , color))