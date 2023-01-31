class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        subs = set()
        
        for i in range(len(s) - k + 1):
            subs.add(s[i:i+k])
        
        if len(subs) == pow(2,k):
            return True
        else:
            return False