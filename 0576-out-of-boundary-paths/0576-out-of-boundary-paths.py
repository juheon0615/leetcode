class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        cache = {}
        
        
        def dfs(i, j, move):
            if move == 0:
                return 0
            
            if (i,j) in cache and move in cache[(i,j)]:
                return cache[(i,j)][move]
            
            
            outs = 0
            
            # up
            if i == 0:
                outs += 1
            else:
                outs += dfs(i-1, j, move - 1)
            
            #down
            if i + 1 == m:
                outs += 1
            else:
                outs += dfs(i+1,j, move - 1)
            
            #left 
            if j == 0:
                outs += 1
            else:
                outs += dfs(i, j-1, move - 1)
            
            #right
            if j + 1 == n:
                outs += 1
            else:
                outs += dfs(i, j+1, move-1)
            
            if (i,j) not in cache:
                cache[(i,j)] = {}
            
            cache[(i,j)][move] = outs
            
            return outs
                
        return dfs(startRow, startColumn, maxMove) % (pow(10,9)+7)
            
                
        
        