class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ret = -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                ret = i
                break
            
        
        return ret
        