class Solution:
    def dfs(self , image , sr , sc , color , oldColor ,  n , m)  :
        
        if sr >= n or sc >= m or sr < 0 or sc < 0 or image[sr][sc] == color or image[sr][sc] != oldColor:
            return
        image[sr][sc] = color
        dire = [[sr+1 , sc] , [sr , sc+1] , [sr-1 , sc] , [sr , sc-1]]
        
        for i , j in dire:
            self.dfs(image , i , j , color , oldColor , n , m)
             
        
    def floodFill(self, image, sr: int, sc: int, color: int):
        n , m = len(image) , len(image[0])
        oldColor = image[sr][sc]
        
        return self.dfs(image , sr , sc , color , oldColor ,  n , m)  
        
        
    

if __name__  == "__main__":
    T = int(input('Test case'))
    for _ in range(T):
        adj = []
        V = int(input('enter the vetex'))
        for i in range(V):
            temp = list(map(int , input('matrix').split()))
            adj.append(temp)
        print(adj)    
        sr , sc = map(int , input('enter sr , sc').split())
        newColor = int(input('enter the color'))
        obj = Solution()
        obj.floodFill(adj, sr, sc, newColor)
        print(adj)
        