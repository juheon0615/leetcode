class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        t = [[0 for _ in range(n)] for __ in range(m)]
        
        
        for i in range(m-1, -1,-1):
            for j in range(n-1, -1, -1):
                p = None
                
                if j < n - 1:
                    p = t[i][j + 1]
                
                if i < m - 1:
                    if p is None:
                        p = t[i + 1][j]
                    else:
                        p = min(p, t[i + 1][j])
                
                # print("i ", i ," j ", j, " p ", p)
                if p is None:
                    t[i][j] = grid[i][j]
                else:
                    t[i][j] = grid[i][j] + p
        # print(t)
        return t[0][0]
        