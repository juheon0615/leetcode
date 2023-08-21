class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ret = []
        m = len(grid)
        n = len(grid[0])
        
        # move left until not neg
        # move down until not pos
        
        def negs(i, j):
            print(i, " : ", j)
            if j > 0 and grid[i][j-1] < 0:
                ret.append(1)
                negs(i,j-1)
            elif i < m - 1 and grid[i+1][j]:
                ret.append(n - j)
                negs(i + 1, j)
        
        si = None
        sj = None
        
        for r, row in enumerate(grid):
            if row[-1] < 0:
                si = r
                sj = len(row) - 1
                break
        
        if si is not None and sj is not None:
            ret.append(1)
            negs(si,sj)
        
        print(ret)
        return sum(ret)
                 
        
        