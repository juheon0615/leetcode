class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        
        for num in nums:
            idx = num
            if idx < 0:
                idx = idx * -1
            idx = idx - 1
            
            if nums[idx] > 0 :
                nums[idx] = nums[idx] * -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i + 1)
        
        return ret