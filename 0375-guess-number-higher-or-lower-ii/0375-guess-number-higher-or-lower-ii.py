class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        
        def dp(low, high):
            if low >= high:
                return 0
            
            if (low, high) in mem:
                return mem[(low,high)]
            
            ret = None
            for i in range(low, high):
                pay = max(dp(low,i-1), dp(i+1,high)) + i
                if ret is None:
                    ret = pay
                else:
                    ret = min(ret, pay)
            
            mem[(low,high)] = ret
            
            return mem[(low,high)]
        
        mem = {}

        return dp(1,n)

        
        
        
                