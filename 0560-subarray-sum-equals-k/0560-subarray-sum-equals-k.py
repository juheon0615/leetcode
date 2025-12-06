class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {}
        acc = 0
        sums[0] = 1
        ret = 0
        for i in range(len(nums)):
            acc += nums[i]

            if (acc - k) in sums:
                ret += sums[acc - k]

            if acc not in sums:
                sums[acc] = 0
            
            sums[acc] += 1
        # print(sums)
        return ret

