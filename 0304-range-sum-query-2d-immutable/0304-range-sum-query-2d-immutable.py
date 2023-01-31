class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        
        row = len(matrix)
        col = len(matrix[0])
        self.aMatrix = [[0 for c in range(col)] for r in range(row)]
        
        for i in range(row):
            for j in range(col):
                val = matrix[i][j]
                if i > 0:
                    val += self.aMatrix[i-1][j]
                if j > 0:
                    val += self.aMatrix[i][j-1]
                
                if i > 0 and j > 0:
                    val -= self.aMatrix[i-1][j-1]
                
                self.aMatrix[i][j] = val        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret = self.aMatrix[row2][col2] 
        
        if row1 > 0:
            ret -= self.aMatrix[row1-1][col2]
        
        if col1 > 0:
            ret -= self.aMatrix[row2][col1-1]
        
        if row1 > 0 and col1 > 0:
            ret += self.aMatrix[row1-1][col1-1]
            
        return ret


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)