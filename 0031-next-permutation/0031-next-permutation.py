class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        swapLeft = i - 1
        
        i = len(nums) - 1
        
        while nums[i] <= nums[swapLeft]:
            i -= 1
        
        swapRight = i
        nums[swapLeft], nums[swapRight] = nums[swapRight], nums[swapLeft]
        
        revLeft = swapLeft + 1
        revRight = len(nums) - 1
        
        while revLeft < revRight:
            nums[revLeft], nums[revRight] = nums[revRight], nums[revLeft]
            revLeft += 1
            revRight -= 1
              
        
        