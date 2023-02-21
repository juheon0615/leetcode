class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        ret = [[0 for _ in range(len(grid[0]))] for __ in range(len(grid))]
        
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                newJ = (j + k) % len(row)
                newI = (i + ((j+k) // len(row))) % len(grid)
                ret[newI][newJ] = num
                
        return ret
        
        