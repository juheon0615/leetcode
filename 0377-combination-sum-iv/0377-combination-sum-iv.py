class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        def dp(cur):
            if cur in mem:
                return mem[cur]
            if cur == 0:
                return 1
            
            ret = 0
            for num in nums:
                if cur - num >= 0:
                    ret += dp(cur - num)
            
            mem[cur] = ret
            return ret
        
        mem = {}
        return dp(target)