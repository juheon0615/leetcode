class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        t = [[0 for _ in range(n)] for __ in range(m)]
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        t[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                
                if j > 0:
                    t[i][j] += t[i][j-1]
                
                if i > 0:
                    t[i][j] += t[i-1][j]
                    
        
        return t[m-1][n-1]
        
        
        
        