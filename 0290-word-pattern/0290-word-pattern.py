class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(words) != len(pattern):
            return False
        
        
        mpw = {}
        mwp = {}
        ret = True
        
        for i, p in enumerate(pattern):
            w = words[i]
            if p in mpw:
                if mpw[p] != w:
                    ret = False
                    break
            elif w in mwp:
                if mwp[w] != p:
                    ret = False
                    break
            else:
                mpw[p] = w
                mwp[w] = p
                
        return ret