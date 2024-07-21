class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[0 for _ in range(n)] for _ in range(m)]

        grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                paths = 0
                if i > 0:
                    paths += grid[i-1][j]
                if j > 0:
                    paths += grid[i][j-1]
                
                if i == 0 and j == 0:
                    paths = 1
                
                grid[i][j] = paths
        # print(grid)
        return grid[m-1][n-1]
