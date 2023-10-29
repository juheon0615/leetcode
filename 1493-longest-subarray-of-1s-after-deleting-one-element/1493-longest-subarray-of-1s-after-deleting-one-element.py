class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        sliding window with left and right
        tolerate one "0"
        keep it in the array
        if new num is 0, update left
        '''
        
        left = right = 0
        maxLength = -math.inf
        zeros = []
        
        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)
                
                if len(zeros) > 1:
                    left = zeros.pop(0) + 1
            
            right = i
            
            maxLength = max(maxLength, right - left)

        return maxLength