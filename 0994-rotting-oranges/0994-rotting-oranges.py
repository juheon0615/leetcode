class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        # bfs then iterate
        
        m = len(grid)
        n = len(grid[0])
        
        q = []
        visited = [[False for _ in range(n)] for __ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        mins = 0

        while q:
            nextQ = []
            while q:
                i, j = q.pop(0)
                                
                # up
                if i > 0 and visited[i-1][j] == False and grid[i-1][j] == 1:
                    nextQ.append((i-1, j))
                    grid[i-1][j] = 2

                # down
                if i < m -1 and visited[i+1][j] == False and grid[i+1][j] == 1:
                    nextQ.append((i+1, j))
                    grid[i+1][j] = 2
                # left
                if j > 0 and visited[i][j-1] == False and grid[i][j-1] == 1:
                    nextQ.append((i, j-1))
                    grid[i][j-1] = 2

                    
                # right
                if j < n - 1 and visited[i][j+1] == False and grid[i][j+1] == 1:
                    nextQ.append((i, j+1))
                    grid[i][j+1] = 2
                    
            q = nextQ
            if nextQ:
                mins += 1

        
        ret = mins
        
        for row in grid:
            for cell in row:
                if cell == 1:
                    ret = -1
                    break
        
        return ret

                
                
        