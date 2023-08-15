class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
                
        l = 1
        r = time[0] * totalTrips
        
        def check(mid):
            trips = 0
            for t in time:
                trips += mid // t
            return True if trips >= totalTrips else False
            
        while l < r:
            
            mid = (l + r) // 2
            
            if check(mid):
                r = mid
            else:
                l = mid + 1
            
        
        
        
        
        return l
            
        