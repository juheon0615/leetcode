class Solution:
    def jump(self, nums: List[int]) -> int:
        ret = 0
        reach = 0
        needJump = 0
        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])

            if i == needJump:
                needJump = reach
                ret += 1
        return ret

        