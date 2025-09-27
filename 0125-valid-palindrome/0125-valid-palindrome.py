class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for c in s:
            if c.isalpha():
                newS += c.lower()
            elif c.isnumeric():
                newS += c
        
        return True if newS == newS[::-1] else False
        
        