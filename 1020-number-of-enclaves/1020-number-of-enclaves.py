class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        notEnclosed = set()
        starts = []
        lands = 0
        
        M = len(grid)
        N = len(grid[0])

        
        for m in range(M):
            for n in range(N):
                if m == 0 or m == M -1 or n == 0 or n == N - 1:
                    if grid[m][n] == 1:
                        starts.append((m,n))
                if grid[m][n] == 1:
                    lands += 1
                    
        def dfs(m,n):
            notEnclosed.add((m,n))
            
            if m + 1 < M and grid[m+1][n] == 1 and (m+1, n) not in notEnclosed:
                dfs(m + 1,n)
            
            if m > 0 and grid[m-1][n] == 1 and (m-1, n) not in notEnclosed:
                dfs(m - 1,n)
            
            if n + 1 < N and grid[m][n+1] == 1 and (m, n+1) not in notEnclosed:
                dfs(m, n + 1)
            
            if n > 0 and grid[m][n-1] == 1 and (m, n-1) not in notEnclosed:
                dfs(m, n - 1)
        
        for start in starts:
            if start not in notEnclosed:
                m,n = start
                dfs(m,n)
        print(notEnclosed)

        return lands - len(notEnclosed)
            
                        
                
        
        
        