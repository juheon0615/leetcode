class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        
        visited = [[False for _ in range(n)] for __ in range(m)]
        
        direction = 0
        
        while len(ret) != (m*n):                
            if direction == 0:
                ret.append(matrix[i][j])
                visited[i][j] = True
                if j == (n-1) or visited[i][j+1]:
                    direction = 1
                    i += 1
                else:
                    j += 1
                
            elif direction == 1:
                ret.append(matrix[i][j])
                visited[i][j] = True
                if i == m - 1 or visited[i+1][j]:
                    direction = 2
                    j -= 1
                else:
                    i += 1
            elif direction == 2:
                ret.append(matrix[i][j])
                visited[i][j] = True
                if j == 0 or visited[i][j - 1]:
                    direction = 3
                    i -= 1
                else:
                    j -= 1
            else:
                ret.append(matrix[i][j])
                visited[i][j] = True
                if i == 0 or visited[i-1][j]:
                    direction = 0
                    j += 1
                else:
                    i -= 1
            
        
        return ret
        