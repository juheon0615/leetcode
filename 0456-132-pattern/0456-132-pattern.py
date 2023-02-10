class Solution:
    def find132pattern(self, nums: List[int]) -> bool: 
        
        
        nk = - pow(10,9)
        s = []
        
        # nums[i] < nk < s[-1]
        # therefore, nk and s[-1] should be maximized 
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < nk:
                return True
            
            while s and nums[i] > s[-1]:
                nk = s.pop(-1)
            
            s.append(nums[i])
        
        return False
            
        
        
        
        
        