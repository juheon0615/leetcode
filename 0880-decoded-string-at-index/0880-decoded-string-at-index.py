class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = 0
        
        for ch in s:
            if ch.isnumeric():
                n *= int(ch)
            else:
                n += 1
        
        for i in range(len(s)-1,-1,-1):
            k %= n
            if k == 0 and s[i].isalpha():
                return s[i]
            
            if s[i].isnumeric():
                n //= int(s[i])
            else:
                n -= 1