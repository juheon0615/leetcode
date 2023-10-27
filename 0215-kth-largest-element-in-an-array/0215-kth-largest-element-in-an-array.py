class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        
        for num in nums:
            heapq.heappush(hq, num)

        n = len(hq) - k
        for _ in range(n):
            heapq.heappop(hq)
        
        return hq[0]
        