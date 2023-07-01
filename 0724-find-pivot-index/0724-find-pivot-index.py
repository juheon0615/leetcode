class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        total = 0
        
        for num in nums:
            total += num
        
        left = 0
        ret = -1
        for i, num in enumerate(nums):
            total -= num            
            
            if left == total:
                ret = i
                break
            
            left += num
        
        return ret
            
            
        