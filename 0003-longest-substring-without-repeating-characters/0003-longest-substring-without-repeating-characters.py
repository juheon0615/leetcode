class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = left = right = 0
        d = {}
        
        for i,c in enumerate(s):
            right = i
            if c in d and d[c] >= left:
                left = d[c] + 1
            d[c] = i
            ret = max(ret, right - left + 1)
        
        return ret
                
        