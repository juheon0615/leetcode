class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rtl = [0 for _ in range(n)]

        rtl[n-1] = nums[n-1]
        for i in range(n - 2, -1, -1):
            rtl[i] = rtl[i+1] * nums[i]
        
        p = np = 1
        for i in range(n-1):
            np *= nums[i]
            nums[i] = p * rtl[i+1]
            p = np

        nums[-1] = p
        return nums