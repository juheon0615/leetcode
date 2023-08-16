class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        n = len(nums)
        def dfs(cur, nums):
            # print(cur, " : ", nums)
            if len(cur) == n:
                ret.append(cur)
                return
            
            
            for i, num in enumerate(nums):
                dfs(cur[:] + [num], nums[:i] + nums[i+1:])
            
        dfs([],nums)
        
        return ret
                
                
                