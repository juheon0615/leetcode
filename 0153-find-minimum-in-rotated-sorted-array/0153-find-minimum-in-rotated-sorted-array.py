class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        '''
        binary search
        
        if mid > right:
            pibot is on right side
        else:
            pivot is on the left side
            
        '''
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]
                
                
        