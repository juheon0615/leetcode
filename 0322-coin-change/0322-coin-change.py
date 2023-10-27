class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None for _ in range(amount+1)]
        
        
        
        dp[0] = 0
        
        for coin in coins:
            for c in range(coin, amount+1):
                if dp[c] is None:
                    dp[c] = dp[c] if dp[c-coin] is None else dp[c-coin] + 1
                else:
                    dp[c] = dp[c] if dp[c-coin] is None else min(dp[c-coin] + 1, dp[c])

        return dp[amount] if dp[amount] is not None else -1
            
            