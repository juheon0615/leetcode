class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ret = [[0 for _ in range(n)] for __ in range(n)]
        
        
        d = 0
        filled = 0
        target = n * n
        
        i = j = 0
        while filled < target:
            filled += 1
            ret[i][j] = filled
            if d == 0:
                if j == n - 1 or ret[i][j+1] != 0:
                    d = 1
                    i += 1
                else:
                    j += 1
            elif d == 1:
                if i == n - 1 or ret[i+1][j] != 0:
                    d = 2
                    j -= 1
                else:
                    i += 1
            elif d == 2:
                if j == 0 or ret[i][j-1] != 0:
                    d = 3
                    i -= 1
                else:
                    j -= 1
            else:
                if i == 0 or ret[i][i-1] != 0:
                    d = 0
                    j += 1
                else:
                    i -= 1
        
        return ret
                
        