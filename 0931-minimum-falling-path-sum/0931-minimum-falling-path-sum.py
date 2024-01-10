class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        
        for i in range (n-2,-1,-1):
            for j in range(n):
                paths = [matrix[i+1][j]]
                
                if j + 1 < n:
                    paths.append(matrix[i+1][j+1])
                
                if j > 0:
                    paths.append(matrix[i+1][j-1])
                
                matrix[i][j] += min(paths)
                
        return min(matrix[0])