class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hn = len(haystack)
        nn = len(needle)

        for i in range(hn-nn+1):
            if haystack[i] == needle[0]:
                if haystack[i:i+nn] == needle:
                    return i
        
        return -1


        