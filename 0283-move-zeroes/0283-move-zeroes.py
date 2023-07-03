class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNum = -1
        
        for i, num in enumerate(nums):
            if num != 0:
                lastNum += 1
                nums[i] = 0
                nums[lastNum] = num
                
                