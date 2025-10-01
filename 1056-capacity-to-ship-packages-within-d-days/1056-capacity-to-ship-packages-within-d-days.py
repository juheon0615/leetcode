class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)

        def canCarry(capacity):
            daysNeeded = 1
            currentWeight = 0
            for weight in weights:
                if weight > capacity:
                    return False
                if currentWeight + weight <= capacity:
                    currentWeight += weight
                else:
                    currentWeight = weight
                    daysNeeded += 1
            return daysNeeded <= days

        while lo < hi:
            mid = (lo + hi) // 2

            if canCarry(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo

        