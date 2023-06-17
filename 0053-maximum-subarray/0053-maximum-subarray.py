class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        find all subarray
        O(n!)
        
        two cursor O(n)
        '''
        
        
        s = 0
        ret = 0
        updated = False
        for i, num in enumerate(nums):
            newS = s + num
            if s + num > 0:
                s += num
                ret = max(ret, s)
                updated = True
            else:
                s = 0
        
        if updated == False:
            ret = nums[0]
            for num in nums:
                ret = max(ret, num)
        
        return ret
        
        