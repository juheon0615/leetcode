class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        left_max = [0 for _ in range(n)]
        right_max = [0 for _ in range(n)]
        
        lm = 0
        for i in range(len(height)):
            left_max[i] = max(lm, height[i])
            lm = max(lm, height[i])
        
        rm = 0
        for i in range(len(height) - 1, -1, -1):
            right_max[i] = max(rm, height[i])
            rm = max(rm, height[i])
        
        for i in range(len(height)):
            water += (min(left_max[i], right_max[i]) - height[i])
        
        
        return water
            
        
        
        