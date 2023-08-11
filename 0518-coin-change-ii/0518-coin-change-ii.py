class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        
        for coin in coins:
            for k in range(coin, amount + 1):
                dp[k] += dp[k - coin]
                
        
        return dp[-1]