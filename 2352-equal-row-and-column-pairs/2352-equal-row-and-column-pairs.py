class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        if there is one 123 in row and two 123 in col, how may pairs are there?
        
        '''
        
        rows = {}
        N = len(grid)
        ret = 0
        
        for i in range(N):
            row = ""
            for j in range(N):
                row += str(grid[i][j]) + " "
            if row not in rows:
                rows[row] = 1
            else:
                rows[row] += 1

        for j in range(N):
            col = ""
            for i in range(N):
                col += str(grid[i][j]) + " "
            if col in rows:
                ret += rows[col]
        
        return ret