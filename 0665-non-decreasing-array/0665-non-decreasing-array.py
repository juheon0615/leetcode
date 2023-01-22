class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ret = True
        changed = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if changed == 1:
                    ret = False
                    break
                
                changed += 1
                
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1] 
        
        
        return ret
                    
        
        