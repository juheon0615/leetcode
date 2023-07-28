class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        def dp(i, cur):
            if (i,cur) in mem:
                return mem[(i,cur)]
            
            if i == len(nums):
                return 1 if cur == target else 0
            
            ret = dp(i+1, cur + nums[i]) + dp(i+1, cur - nums[i])
            
            mem[(i,cur)] = ret
            return mem[(i,cur)]
            
        mem = {}
        
        ret = dp(0,0)
        return ret