class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # flip diagonal then horizonal
        
        for i in range(len(matrix)):
            for j in range(len(matrix) - i - 1):
                temp = matrix[i][j]
                ii = len(matrix) - j - 1
                jj = len(matrix) - i - 1
                
                matrix[i][j] = matrix[ii][jj]
                matrix[ii][jj] = temp
        
        for i in range(len(matrix) // 2):
            for j in range(len(matrix)):
                temp = matrix[i][j]
                ii = len(matrix) - i - 1
                jj = j
                
                matrix[i][j] = matrix[ii][jj]
                matrix[ii][jj] = temp
                                
                
        