class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ret = []
        
        s = newInterval[0]
        e = newInterval[1]
        
        for interval in intervals:            
            if s is not None and e is not None:
                if interval[1] < s:
                    ret.append(interval)
                elif interval[0] > e:                    
                    ret.append([s,e])
                    ret.append(interval)
                    s = e = None
                else:
                    s = min(s, interval[0])
                    e = max(e, interval[1])
            else:
                ret.append(interval)
        
        if s is not None and e is not None:
            ret.append([s,e])
        
        return ret