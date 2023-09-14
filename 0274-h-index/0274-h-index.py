class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        hs = [0 for _ in range(1001)]
        
        for c in citations:
            hs[c] += 1
            
        
        
        for i in range(len(hs) - 2, -1, -1):
            hs[i] += hs[i+1]
        
        ret = 0
        for i in range(len(hs)):
            if i <= hs[i]:
                ret = max(ret, i)
        
        
        return ret
            
            
            
        
        
        
        