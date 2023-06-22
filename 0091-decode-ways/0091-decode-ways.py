class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        def dp(i, mem):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
                
            
            if i in mem:
                return mem[i]
            
            
            
            ret = 0
            
            ret = dp(i+1,mem)
            
            if i < len(s) -1 and 0 < int(s[i] + s[i+1]) < 27:
                ret += dp(i+2,mem)
            
            
            mem[i] = ret
            
            return mem[i]
        
        mem = {}
        return dp(0,mem)
            
            
        
        