class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(amt, mem):
            if amt in mem:
                return mem[amt]
            
            if amt == 0:
                return True, 0
            
            found = False
            ret = None
            
            for coin in coins:
                if amt >= coin:
                    f, r = dp(amt-coin, mem)
                    if f is True:
                        if ret is None:
                            found = f
                            ret = r + 1
                        else:
                            found = f
                            ret = min(ret, r + 1)
            
            mem[amt] = (found, ret)
            
            return mem[amt]
        
        mem = {}
        
        found, ret = dp(amount, mem)
        # print(mem)
        return ret if found == True else -1
        
        
        
                        
            
            