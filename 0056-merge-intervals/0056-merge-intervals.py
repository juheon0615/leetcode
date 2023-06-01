class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        
        cur = None
        
        for interval in intervals:
            if cur is None:
                cur = interval
            else:
                if cur[1] >= interval[0]:
                    cur[0] = min(cur[0], interval[0])
                    cur[1] = max(cur[1], interval[1])
                else:
                    ret.append(cur)
                    cur = interval
        
        if cur is not None:
            ret.append(cur)
        return ret