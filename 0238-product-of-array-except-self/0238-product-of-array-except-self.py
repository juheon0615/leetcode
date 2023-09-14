class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        output = [1 for _ in range(len(nums))]
        
        
        products = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = products
            products *= nums[i]
        
        products = 1
        for i in range(len(nums)):
            output[i] *= products
            products *= nums[i]
        
        return output
        
        
        