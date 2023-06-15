class Solution:
    def dfs(self, nums, cur, target, ret):
        if target == 0:
            ret.append(cur)
            return

        if target < 0:
            return


        for i, num in enumerate(nums):
            self.dfs(nums[i:], cur[:] + [nums[i]], target - nums[i], ret)
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ret = []
        self.dfs(candidates, [], target, ret)

        return ret
            