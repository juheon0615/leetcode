class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for r, row in enumerate(triangle):
            if r == 0:
                continue
            
            for i, num in enumerate(row):
                if i == 0:
                    row[i] += triangle[r-1][0]
                elif i == len(row) - 1:
                    row[i] += triangle[r-1][-1]
                else:
                    row[i] += min(triangle[r-1][i-1], triangle[r-1][i])
            
        ret = None
        
        for i, num in enumerate(triangle[-1]):
            if i == 0:
                ret = num
            else:
                ret = min(ret, num)
        
        return ret
            
        