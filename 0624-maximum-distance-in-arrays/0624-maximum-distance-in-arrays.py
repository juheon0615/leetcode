class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        curMin = arrays[0][0]
        curMax = arrays[0][-1]
            
        maxDiff = -math.inf
        
        for i in range(1, len(arrays)):
            maxDiff = max(maxDiff, abs(curMax - arrays[i][0]), abs(arrays[i][-1] - curMin))
            curMax = max(curMax, arrays[i][-1])
            curMin = min(curMin, arrays[i][0])
        
        return maxDiff
            
        
        