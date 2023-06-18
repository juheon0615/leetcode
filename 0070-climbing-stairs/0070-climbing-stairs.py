class Solution:
    def climbStairs(self, n: int) -> int:
        '''

        1 1 1 
        1 2
        2 1
        
        
        '''
        
        mem = {}
        def dp(n):
            if n in mem:
                return mem[n]
            
            if n == 0:
                return 1
            
            if n < 0:
                return 0
            
            ret = 0
            for i in range(1, 3):
                ret += dp(n - i)
            
            
            mem[n] = ret
            return ret
    
        return dp(n)
        
        
                