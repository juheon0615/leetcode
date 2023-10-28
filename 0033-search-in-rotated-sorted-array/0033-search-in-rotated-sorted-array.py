class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        '''
        if nums[l] <= nums[r]: normal bsearch
        if nums[mid] <= nums[r]: normal bsearch
        if nums[mid] > nums[r]: pivot in [mid:r]
        if nums[mid] >= nums[l]: normal bsearch
        if nums[mid] < nums[l]: pivot in [l:mid]
        
        
        '''
        
        
        def bsearch(left, right, nums, target):
            if left > right:
                return -1
            
            mid = left + (right - left) // 2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if nums[mid] < nums[left] and target > nums[right]:
                    return bsearch(left, mid-1, nums, target)
                else:
                    return bsearch(mid+1, right, nums, target)
            else:
                if nums[mid] > nums[right] and target < nums[left]:
                    return bsearch(mid+1, right, nums, target)
                else:
                    return bsearch(left, mid-1, nums, target)
        
        return bsearch(0, len(nums)-1, nums, target)
        
        