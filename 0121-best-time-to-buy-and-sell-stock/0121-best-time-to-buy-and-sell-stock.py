class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        bought = None
        for price in prices:
            if bought is None:
                bought = price
            else:
                ret = max(ret, price - bought)
                bought = min(bought, price)
                # print("%d %d %d" %(bought, price, ret))
        
        
        return ret
        