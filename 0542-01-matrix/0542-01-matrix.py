class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        q = []
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited[i][j] = True
        
        
        ret = [[0 for _ in range(n)] for _ in range(m)]

        d = 0
        while q:
            nextQ = []
            
            for i,j in q:
                if mat[i][j] > 0:
                    ret[i][j] = d
                
                # up i - 1
                if i > 0 and visited[i-1][j] == False:
                    visited[i-1][j] = True
                    nextQ.append((i-1, j))
                
                
                # down
                if i < m-1 and visited[i+1][j] == False:
                    visited[i+1][j] = True
                    nextQ.append((i+1, j))
                
                # left
                if j > 0 and visited[i][j-1] == False:
                    visited[i][j-1] = True
                    nextQ.append((i, j-1))
                
                # right
                if j < n-1 and visited[i][j+1] == False:
                    visited[i][j+1] = True
                    nextQ.append((i,j+1))
            
            q = nextQ
            d += 1

            
        return ret
            
        