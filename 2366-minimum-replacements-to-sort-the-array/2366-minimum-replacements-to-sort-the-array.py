class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        
        ret = 0
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= nums[i+1]:
                continue
             
            num = (nums[i] + nums[i+1] - 1) // nums[i+1]
            
            ret += num - 1
            
            nums[i] = nums[i] // num
            
        return ret