class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d = {}
        ret = 0
        
        for i,c in enumerate(s):
            if c in d:
                if d[c] + 1 >= left:
                    left = d[c] + 1
            
            d[c] = i
            ret = max(ret, i - left + 1)
        
        return ret
                
        