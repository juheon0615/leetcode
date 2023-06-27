class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        begin = None
        end = None
        merged = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        
        for interval in intervals:
            if begin is None:
                begin = interval[0]
                end = interval[1]
            else:
                if end < interval[0]:
                    merged.append([begin,end])
                    begin = interval[0]
                    end = interval[1]
                else:
                    end = max(end, interval[1])
        
        if begin is not None:
            merged.append([begin,end])
        
                
        
        
        return merged