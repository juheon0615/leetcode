class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        
        s,e = intervals[0]
        ret = []
        
        for interval in intervals:
            ss, ee = interval
            
            if s == ss:
                e = max(e,ee)
            elif s < ss <= e:
                e = max(e,ee)
            else:
                ret.append([s,e])
                s = ss
                e = ee
        ret.append([s,e])
        
        return ret
        