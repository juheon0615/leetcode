class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0 for i in range(n)]
        rightMax = [0 for i in range(n)]

        left = 0
        for i in range(n):
            leftMax[i] = left
            left = max(left, height[i])        
        right = 0
        for i in range(n-1, -1, -1):
            rightMax[i] = right
            right = max(right, height[i])
        
        ret = 0
        for i in range(n):
            if leftMax[i] > height[i] < rightMax[i]:
                ret += (min(leftMax[i], rightMax[i]) - height[i])
        return ret

        
