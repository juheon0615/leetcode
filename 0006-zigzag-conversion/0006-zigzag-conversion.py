class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ret = ""
        if numRows == 1: 
            return s
        
        for r in range(numRows):
            i = r

            while i < len(s):
                if r == 0 or r == numRows - 1:
                    ret += s[i]
                else:
                    ret += s[i]
                    offset = numRows - r + numRows  -  r  - 2
                    if i + offset < len(s):
                        ret += s[i+offset]
                i += numRows + numRows - 2
                if i == 0:
                    break
            
        return ret

        