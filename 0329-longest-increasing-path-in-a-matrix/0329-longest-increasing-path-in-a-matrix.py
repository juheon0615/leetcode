class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         def dfs(i, j):
#             print(i, " ", j)
#             if not dp[i][j]:
#                 val = matrix[i][j]
#                 dp[i][j] = 1 + max(
#                     dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
#                     dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
#                     dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
#                     dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
#             return dp[i][j]

#         if not matrix or not matrix[0]: return 0
#         M, N = len(matrix), len(matrix[0])
#         dp = [[0] * N for i in range(M)]
#         return max(dfs(x, y) for x in range(M) for y in range(N))
        
        def dfs(i, j, dp):
            if dp[i][j] > 0:
                return dp[i][j]
               
            ret = 0
            
            #up
            if i > 0 and matrix[i][j] < matrix[i - 1][j]:
                ret = max(ret, dfs(i - 1, j, dp))
            #down
            if i < len(matrix) - 1 and matrix[i][j] < matrix[i + 1][j]:
                ret = max(ret, dfs(i + 1, j, dp))
            
            #left
            if j > 0 and matrix[i][j] < matrix[i][j - 1]:
                ret = max(ret, dfs(i, j - 1, dp))
            
            #right
            if j < len(matrix[0]) - 1 and matrix[i][j] < matrix[i][j + 1]:
                ret = max(ret, dfs(i, j + 1, dp))  
                          

            ret += 1
            dp[i][j] = ret

            return dp[i][j] 
        
        
        ans = 0
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        for i in range(M):
            for j in range(N):
                ans = max(ans, dfs(i,j, dp))
        
        
        return ans
                
                
        
                          

            
            
        