class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        ret = []
        d = {}
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub not in d:
                d[sub] = 0
            
            d[sub] += 1
        
        
        for (key,val) in d.items():
            if val > 1:
                ret.append(key)
        
        return ret
        