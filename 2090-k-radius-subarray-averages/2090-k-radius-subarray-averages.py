class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        rsums = [0 for _ in range(len(nums))]
        lsums = [0 for _ in range(len(nums))]
        ret = [0 for _ in range(len(nums))]
        
        rsum = 0
        for i in range(len(nums)):
            if i - k - 1 >= 0:
                rsum -= nums[i-k-1]
            
            rsum += nums[i]
            
            rsums[i] = rsum    
        
        lsum = 0
        for i in range(len(nums) - 1, -1, -1):
            if i + k + 1 < len(nums):
                lsum -= nums[i + k + 1]
            
            lsum += nums[i]
            lsums[i] = lsum
        
        
        for i in range(len(nums)):
            if i - k  >= 0 and i + k  < len(nums):
                div = k * 2 + 1
                ret[i] = (rsums[i] + lsums[i] - nums[i]) // div
            else:
                ret[i] = -1
        # print(rsums)
        # print(lsums)
        # print(ret)
        return ret 
        