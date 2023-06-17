class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        t = [[0 for _ in range(n)] for __ in range(m)]
        
        t[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i > 0:
                    t[i][j] += t[i-1][j]
                
                if j > 0:
                    t[i][j] += t[i][j-1]
        
        return t[m-1][n-1]