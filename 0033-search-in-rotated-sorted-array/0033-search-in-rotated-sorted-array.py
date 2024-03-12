class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        case left < right no pivot between left and right
        - if mid == target return mid
        - if mid > target search(left, mid - 1) else serach(mid + 1, right)
        
        case left > right pivot between left and right 5, 6, 1, 2, 3, 4
        - if mid == target return
        - if mid < target and less than right serach(mid + 1, right)
        - if mid < target and greater than right serach(left, mid - 1)
        - if mid > target and mid - 1 and left
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