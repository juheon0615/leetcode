class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        amap = {}
        for i, alphabet in enumerate(alphabets):
            amap[i] = alphabet
            
        ret = ""
        
        n = columnNumber
        while n > 0:
            n -= 1
            ret += amap[n % len(alphabets)]
            n = n // len(alphabets)
        
        return ret[::-1]
            