class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0, 0, 0] for _ in range(n+1)]

        for i, cost in enumerate(costs):
            dp[i+1][0] = min(dp[i][1], dp[i][2]) + cost[0]
            dp[i+1][1] = min(dp[i][0], dp[i][2]) + cost[1]
            dp[i+1][2] = min(dp[i][0], dp[i][1]) + cost[2]
        
        return min(dp[-1])

        