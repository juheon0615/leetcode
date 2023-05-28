class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        sxr = str(sx)[::-1]
        
        return True if sx == sxr else False
        