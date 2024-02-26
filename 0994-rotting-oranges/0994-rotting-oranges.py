class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        M = len(grid)
        N = len(grid[0])
        rottens = []
        visited = set()
        
        
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 2:
                    rottens.append([m, n])
                    visited.add((m,n))
        
        ret = 0
        while rottens:
            # print(rottens)
            q = []
            for rotten in rottens:
                m, n = rotten
                
                for move in moves:
                    mm = m + move[0]
                    nn = n + move[1]
                    
                    if 0 <= mm < M and 0 <= nn < N and grid[mm][nn] == 1 and (mm,nn) not in visited:
                        q.append([mm,nn])
                        visited.add((mm,nn))
                        grid[mm][nn] = 2
            rottens = q
            if len(rottens) > 0:
                ret += 1
        
        # print(grid)
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1:
                    ret = -1
        
        return ret
        
        
                
        
        
        
        