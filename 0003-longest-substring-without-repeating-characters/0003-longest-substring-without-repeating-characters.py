class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        start = 0
        ret = 0
        for i,c in enumerate(s):
            if c in last and last[c] >= start:
                start = last[c] + 1

            last[c] = i
            ret = max(ret, i - start + 1)
        
        return ret
                