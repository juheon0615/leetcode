class Solution:
    def romanToInt(self, s: str) -> int:
        syms = { "M" : 1000, "D" : 500,  "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1 }
        
        ret = 0
        lastVal = 1000
        
        for c in s:
            if syms[c] > lastVal:
                ret -= lastVal
                ret += (syms[c] - lastVal)
            else:
                ret += syms[c]
            lastVal = syms[c]
        
        return ret
            
            
            
        