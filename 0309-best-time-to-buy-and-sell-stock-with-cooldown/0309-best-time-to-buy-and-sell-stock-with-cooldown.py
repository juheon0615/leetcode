class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dp(i, hold, mem):
            if (i,hold) in mem:
                return mem[(i,hold)]
            
            if i >= len(prices):
                return 0
            
            ret = 0
            if hold is None:
                ret = max(ret, dp(i+1, None, mem), dp(i+1, prices[i],mem))
            
            else:   
                if hold < prices[i]:
                    ret = max(ret, dp(i + 2, None, mem) + (prices[i] - hold), dp(i+1, hold, mem))
                else:
                    ret = max(ret, dp(i + 1, prices[i], mem))
            
            mem[(i,hold)] = ret
            
            # print(mem)
            return mem[(i,hold)]
        
        
        mem = {}
        
        
        return dp(0,None,mem)
            
            
            
            
        