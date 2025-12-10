class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        heap = []


        for slot in slots1:
            heapq.heappush(heap, slot)
        for slot in slots2:
            heapq.heappush(heap, slot)
        
        while len(heap) > 1:
            start1, end1 = heapq.heappop(heap)
            start2, end2 = heapq.heappop(heap)
            # print("start1[%d, %d] start2[%d, %d]" % (start1,end1,start2,end2))
            if max(start1,start2) + duration <= min(end1, end2):
                return [max(start1,start2), max(start1,start2) + duration]
            else:
                if end1 > end2:
                    heapq.heappush(heap, [start1, end1])
                else:
                    heapq.heappush(heap, [start2, end2])
        
        return []

        