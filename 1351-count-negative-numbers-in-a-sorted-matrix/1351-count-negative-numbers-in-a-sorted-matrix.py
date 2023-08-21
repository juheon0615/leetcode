class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ret = 0
        m = len(grid)
        n = len(grid[0])
        
        # move left until not neg
        # move down until not pos
        
        def negs(i, j):
            nonlocal ret
            
            if j > 0 and grid[i][j-1] < 0:
                ret += 1
                negs(i,j-1)
            elif i < m - 1 and grid[i+1][j]:
                ret += n - j
                negs(i + 1, j)
        
        si = None
        sj = None
        
        for r, row in enumerate(grid):
            if row[-1] < 0:
                si = r
                sj = len(row) - 1
                break
        
        if si is not None and sj is not None:
            ret += 1
            negs(si,sj)
        
        return ret
                 
        
        