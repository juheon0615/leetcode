class Solution:
    def reverse(self, x: int) -> int:
        sx = str(x)
        
        isNeg = False
        
        if sx[0] == "-":
            isNeg = True
            sx = sx[1:]
        
        sx = sx[::-1]
        sx = sx.lstrip("0")
        
        if len(sx) == 0:
            sx = "0"
        
        if isNeg:
            sx = "-" + sx
        
        ret = int(sx)
        
        if ret < pow(-2,31) or ret > pow(2,31) - 1:
            ret = 0
            
        return ret
        
        
        