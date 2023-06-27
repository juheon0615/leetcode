class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for i, s in enumerate(strs):
            ss = ''.join(sorted(s))
            if ss not in groups:
                groups[ss] = []
            
            groups[ss].append(i)
        
        ret = []
        for (group, index) in groups.items():
            r = []
            for i in index:
                r.append(strs[i])
            
            ret.append(r)
        
        return ret
                
        
                
        
        