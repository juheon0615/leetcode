class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dp(i, hasFirst, mem):
            if i >= len(nums):
                return 0
            
            if i == len(nums) - 1:
                return 0 if hasFirst else nums[i]
            
            if i in mem and hasFirst in mem[i]:
                return mem[i][hasFirst] 
            
            ret = 0
            if i == 0:
                ret = max(dp(i+1, False, mem), dp(i+2, True, mem) + nums[i])
            else:
                ret = max(dp(i+1, hasFirst, mem), dp(i+2, hasFirst, mem) + nums[i])
                
            if i not in mem:
                mem[i] = {}
            
            mem[i][hasFirst] = ret
            return mem[i][hasFirst] 
        
        mem = {}
        ret = dp(0, False, mem)
        
        # print(mem)
        return ret