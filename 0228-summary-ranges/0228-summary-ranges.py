class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        start = end = None
        ret = []
        
        for num in nums:
            if start is None:
                start = num
                end = num
            else:
                if end + 1 == num:
                    end = num
                else:
                    if start == end:
                        ret.append("%d"%(start))
                    else:
                        ret.append("%d->%d" %(start,end))                    
                    start = end = num
        
        
        if start == end:
            ret.append("%d"%(start))
        else:
            ret.append("%d->%d" %(start,end))
                    
        return ret