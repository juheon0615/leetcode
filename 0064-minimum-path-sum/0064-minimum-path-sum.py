class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[math.inf for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]

        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
                
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])

        # print(dp)

        return dp[-1][-1]
        