class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        ret = 0
        for i in range(len(nums)):
            minVal, maxVal = math.inf, -math.inf

            for j in range(i, len(nums)):
                
                minVal = min(minVal, nums[j])
                maxVal = max(maxVal, nums[j])
                
                ret += (maxVal - minVal)
        
        return ret
                