class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        
        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1
        
        heap = []

        for num, freq in freqs.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                popped = heapq.heappop(heap)
        
        ret = [num for _, num in heap ]

        return ret
        