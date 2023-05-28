class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for _ in range(numRows)]
        cur = 0
        zigUp = False
        for c in s:
            rows[cur] += c
            
            if numRows == 1:
                continue
            
            if zigUp:
                if cur == 0:
                    cur += 1
                    zigUp = False
                else:
                    cur -= 1
            else:
                if cur == numRows - 1:
                    cur -= 1
                    zigUp = True
                else:
                    cur += 1
        
        ret = ""
        for row in rows:
            ret += row
        
        return ret
            
        
        