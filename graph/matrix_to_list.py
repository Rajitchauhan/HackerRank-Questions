from  collections import defaultdict
class MatToList:
    def mat(self):
        T = int(input('enter number  of test cases'))
        
        for _ in range(T):
            adj = []
            V = int(input('enter number of vartex'))
            for i  in range(V):
                temp = list(map(int , input('enter matrix row').split()))
                adj.append(temp)
            print(adj)
            self.convertMat(V , adj)
    def convertMat(self , V , adj):
        nadj = defaultdict(list)
        n = len(adj)
        
        for i in range(n):
            for j  in range(i+1  , n):
                if(adj[i][j] == 1):
                    nadj[i].append(j)
                    nadj[j].append(i)
        print(nadj)
        for u , v in nadj.items():
            print(f' {u} -> {v}')
            
            
obj = MatToList()
obj.mat()
