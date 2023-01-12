import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int: 
        engineers = []
        
        for i in range(len(speed)):
            engineers.append([speed[i], efficiency[i]])
        
        # sort by efficiency
        engineers.sort(key=lambda x:x[1], reverse=True)
        
        
        
        heap = []
        res = 0
        speeds = 0
        
        for engineer in engineers:
            heapq.heappush(heap, engineer[0])
            speeds += engineer[0]
            if len(heap) > k:
                speeds -= heapq.heappop(heap)
            res = max(res, speeds * engineer[1])
        return res % (10**9 + 7)            
        
        
        
        
        