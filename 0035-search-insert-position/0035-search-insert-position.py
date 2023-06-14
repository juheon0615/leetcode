class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        ret = None
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                ret = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        #024 -> i1 > l = 1 r =0 t = 1
        #024 -> i3 > l = 2 r =1 t = 2
        #024 -> i-1 > l = 0 r = -1 t= 0
        #024 -> i5 > l = 3 r = 2 t =3
        
        if ret is None:
            ret = l
        
        return ret