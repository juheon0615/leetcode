class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        sliding window with 0 counts...
        must keep the indexes of 0s
        if 0 count > 0 with new i, window left = zeros[0]. zero.pop(0)
        
        '''
        
        
        left = right = 0
        maxLength = -math.inf
        zeros = []
        
        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)
                if len(zeros) > k:
                    left = zeros.pop(0) + 1
            right = i
            maxLength = max(maxLength, right - left + 1)
            
        
        return maxLength