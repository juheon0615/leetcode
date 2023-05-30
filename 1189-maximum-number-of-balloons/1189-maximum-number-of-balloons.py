class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for c in text:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        ret = len(text)
        
        if "b" in d:
            ret = min(ret, d["b"])
        else:
            ret = 0
        
        if "a" in d:
            ret = min(ret, d["a"])     
        else:
            ret = 0
            
        if "l" in d:
            ret = min(ret, d["l"] // 2)
        else: 
            ret = 0
            
        if "o" in d:
            ret = min(ret, d["o"] // 2)
        else:
            ret = 0
            
        if "n" in d:
            ret = min(ret, d["n"])
        else:
            ret = 0
            
        return ret