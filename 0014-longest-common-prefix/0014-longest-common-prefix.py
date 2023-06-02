class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        cur = strs[0]
        for s in strs:
            if len(cur) > len(s):
                cur = s
        
        ret = ""
        for i,c in enumerate(cur):
            p = True
            for s in strs:
                if s[0:i+1] != cur[0:i+1]:
                    p = False
                    break
            
            if p:
                ret = cur[0:i+1]
            else:
                break
                
        
        return ret
        