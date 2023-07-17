class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        cnts = {}
        for num in nums:
            if num not in cnts:
                cnts[num] = 0
            cnts[num] += num
        
        
        N = 10**4
        dp = [0 for _ in range(N + 1)]
        dp[0] = 0 if 0 not in cnts else cnts[0]
        dp[1] = dp[0] if 1 not in cnts else max(dp[0], cnts[1])
        
        
        for i in range(2, N + 1):
            val = 0 if i not in cnts else cnts[i]
            dp[i] = max(dp[i-1], dp[i-2] + val)
            
        
        
        # print(dp)
        
        
        return dp[-1]
        