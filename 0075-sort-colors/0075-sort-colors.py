class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        cnts = [0,0,0]
        
        for num in nums:
            cnts[num] += 1
            
        def getNextValue(i):
            if i < cnts[0]:
                return 0
            elif i < cnts[0] + cnts[1]:
                return 1
            elif i < cnts[0] + cnts[1] + cnts[2]:
                return 2
            else:
                return -1
        
        for i, num in enumerate(nums):
            nums[i] = getNextValue(i)
            