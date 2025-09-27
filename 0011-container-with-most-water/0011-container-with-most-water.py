class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1

        ret = 0
        while i < j:
            ret = max(ret, ((j - i) * min(height[i], height[j])))
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                i += 1
                j -= 1
        return ret
