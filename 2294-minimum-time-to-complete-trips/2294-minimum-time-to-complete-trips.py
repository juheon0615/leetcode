class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        hi = min(time) * totalTrips
        lo = 0

        def canCompletTrip(timeLimit):
            numberOfTripsMadeInT = sum(timeLimit // t for t in time)
            return True if numberOfTripsMadeInT >= totalTrips else False

        while lo < hi:
            mid = (lo + hi) // 2
            
            if canCompletTrip(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo






