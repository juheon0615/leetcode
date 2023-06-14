class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        find the start
        find the end
        
        start
        
        '''

        l = 0
        r = len(nums) - 1
        #011
        #012
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] < target:
                l = mid + 1
            else:   
                r = mid - 1
        
        low = l
        
        l = 0 
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
            
        high = r
        
        # print(low, " : ", high)
        if low > high:
            return [-1,-1]
        else:
            return [low, high]
        
                
            
        
            