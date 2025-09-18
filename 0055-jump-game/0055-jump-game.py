class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ret = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= ret:
                ret = i

        return ret == 0

        