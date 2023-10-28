class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        M = len(grid)
        N = len(grid[0])
        visited = set()

        def dfs(m,n):
            visited.add((m,n))
            
            dm = [0, 0, 1, -1]
            dn = [1, -1, 0, 0]
            
            closed = True
            
            if m == 0 or n == 0 or m == M -1 or n == N - 1:
                closed = False
            
            land = 1
            
            for i in range(len(dm)):
                mm = m + dm[i]
                nn = n + dn[i]
                
                if 0 <= mm < M and 0 <= nn < N and (mm,nn) not in visited and grid[mm][nn] == 0:
                    l, c = dfs(mm,nn)
                    land += l
                    closed = closed & c
            
            return land, closed
    
        ret = 0
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 0 and (m,n) not in visited:
                    land, closed = dfs(m,n)
                    if closed:
                        # print(m," : ",n)
                        ret += 1
        
        return ret
        