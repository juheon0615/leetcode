class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False for _ in range(n)] for __ in range(m)]
        islands = [[0 for _ in range(n)] for __ in range(m)]

        lands = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    lands.append((i,j))
        
        
        def dfs(i,j):
            visited[i][j] = True
            
            if i > 0 and grid[i-1][j] == "1" and visited[i-1][j] == False:
                dfs(i-1, j)
            
            if i < m - 1 and grid[i+1][j] == "1" and visited[i+1][j] == False:
                dfs(i+1, j)
            
            if j > 0 and grid[i][j-1] == "1" and visited[i][j-1] == False:
                dfs(i, j-1)
            
            if j < n - 1 and grid[i][j+1] == "1" and visited[i][j+1] == False:
                dfs(i, j+1)
        
        ret = 0
        for land in lands:
            i = land[0]
            j = land[1]
            if visited[i][j] == False:
                dfs(i,j)
                ret += 1
        print(visited)
        return ret
            
            
                    
        