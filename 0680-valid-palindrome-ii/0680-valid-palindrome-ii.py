class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        deleted = 0
        ret = True
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                deleted += 1
                i += 1

                if deleted > 1:
                    ret = False
                    break
        
        if ret:
            return ret
        
        
        i = 0
        j = len(s) - 1
        deleted = 0
        ret = True
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                deleted += 1
                j -= 1

                if deleted > 1:
                    ret = False
                    break
        
        return ret
                    
            
            
        