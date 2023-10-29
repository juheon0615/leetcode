class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        slide windows. if incoming char is vowl, increment vowl counter, if outgoing char is vowel decrement vowel counter
        '''
        
        
        maxCount = -math.inf
        vowels = set(["o", "u", "i","e", "a"])
        currentCount = 0
        for i,c in enumerate(s):
            if c in vowels:
                currentCount += 1
            
            if i >= k and s[i-k] in vowels:
                currentCount -= 1
            
            if i >= k - 1:
                maxCount = max(maxCount, currentCount)
        
        return maxCount
                
            
            
            
        