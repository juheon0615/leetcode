class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        up = False
        hold = None
        profit = 0
        
        
        
        for i, price in enumerate(prices):

            if i == len(prices) - 1:
                if up:
                    profit += price - hold
            else:
                if price <= prices[i+1]:
                    if up:
                        pass
                    else:
                        up = True
                        hold = price
                else:
                    if up:
                        if hold is not None:
                            profit += price - hold
                        up = False
                    else:
                        hold = price
                    
            # print("i ", i, " price ", price, " hold ", hold, " profit ", profit)

        return profit
            

        

        
            