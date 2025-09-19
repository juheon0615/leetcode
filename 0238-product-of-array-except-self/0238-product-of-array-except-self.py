class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ltr = [0 for _ in range(n)]
        rtl = [0 for _ in range(n)]
        ret = [0 for _ in range(n)]

        ltr[0] = nums[0]
        for i in range(1, n):
            ltr[i] = ltr[i-1] * nums[i]
        
        rtl[n-1] = nums[n-1]
        for i in range(n - 2, -1, -1):
            rtl[i] = rtl[i+1] * nums[i]
        
        ret[0] = rtl[1]
        ret[n-1] = ltr[n-2]

        for i in range(1, n-1):
            ret[i] = ltr[i-1] * rtl[i+1]

        return ret