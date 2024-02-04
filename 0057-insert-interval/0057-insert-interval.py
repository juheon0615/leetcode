class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        ret = []
        ns = newInterval[0]
        ne = newInterval[1]
        for interval in intervals:
            s = interval[0]
            e = interval[1]
            
            if ns is None:
                ret.append([s,e])
                continue
            
            if e < ns:
                ret.append([s,e])
            elif s > ne:
                ret.append([ns,ne])
                ret.append([s,e])
                ns = None
                ne = None
            else:
                ns = min(ns,s)
                ne = max(ne,e)
        
        if ns is not None:
            ret.append([ns,ne])
            
            
        return ret