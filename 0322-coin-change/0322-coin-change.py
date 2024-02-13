class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        changes = [None for _ in range(amount+1)]
        changes[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                if changes[i - coin] is not None:
                    if changes[i] is None:
                        changes[i] = changes[i - coin] + 1
                    else:
                        changes[i] = min(changes[i], changes[i - coin] + 1)
        
        return -1 if changes[amount] is None else changes[amount]
        
        