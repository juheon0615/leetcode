class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret = -math.inf

        i = 0
        j = len(height) - 1

        while i < j:
            area = min(height[i], height[j]) * (j-i)
            ret = max(ret, area)

            if height[i] == height[j]:
                i += 1
                j -= 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return ret
