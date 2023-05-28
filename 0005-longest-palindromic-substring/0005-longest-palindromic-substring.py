class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        
        for i,c in enumerate(s):
            left = i - 1
            right = i + 1
            cur = c
            
            while left >=0 and right < len(s):
                if s[left] == s[right]:
                    cur = s[left] + cur + s[right]
                    left -= 1
                    right += 1
                else:
                    break
            
            if len(cur) > len(ret):
                ret = cur
            
            
            left = i
            right = i+1
            cur = ""
            
            while left >=0 and right < len(s):
                if s[left] == s[right]:
                    cur = s[left] + cur + s[right]
                    left -= 1
                    right += 1
                else:
                    break
            
            if len(cur) > len(ret):
                ret = cur
                        
        return ret
            
            
        