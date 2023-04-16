class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if sum(nums[i:j]) % k == 0 for some i < j 
        # sum(nums[:j]) % k == sum(nums[:i]) % k
        # solution array range is [d[s] + 1 : i]
        d , s = {0:-1} , 0
        for i, n in enumerate(nums):
            if k != 0:
                s = (s + n) % k
            else:
                s += n
            if s not in d:
                d[s] = i
            else:
                if i - d[s] >= 2:
                    return True
        return False