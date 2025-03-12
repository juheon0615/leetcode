class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                    continue
                
                if i > 0:
                    obstacleGrid[i][j] += obstacleGrid[i-1][j]
                if j > 0:
                    obstacleGrid[i][j] += obstacleGrid[i][j-1]
        # print(dp)
        return obstacleGrid[-1][-1]


        