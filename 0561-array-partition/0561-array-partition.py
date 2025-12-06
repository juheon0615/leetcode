class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        ret = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ret += nums[i]
        return ret
        