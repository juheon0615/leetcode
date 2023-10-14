class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        st = {}
        ts = {}
        
        ret = True
        
        
        
        for i in range(len(s)):
            if s[i] not in st:
                st[s[i]] = t[i]
            else:
                if st[s[i]] != t[i]:
                    ret = False
                    break
            
            if t[i] not in ts:
                ts[t[i]] = s[i]
            else:
                if ts[t[i]] != s[i]:
                    ret = False
                    break
                
        
        return ret
            
        