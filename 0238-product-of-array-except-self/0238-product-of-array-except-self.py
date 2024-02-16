class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        lr = [num for num in nums]
        rl = [num for num in nums]
        
        
        for i in range(1, N):
            lr[i] = lr[i-1] * lr[i]
        
        for i in range(N - 2, -1, -1):
            rl[i] = rl[i+1] * rl[i]
        
        
        for i in range(0, N):
            left = 1 if i == 0 else lr[i-1]
            right = 1 if i == N - 1 else rl[i+1]
            
            nums[i] = left * right
            
            
        return nums
            
        
        