class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[0])

        heap = []
        ret = 0
        for interval in intervals:
            start, end = interval
            while heap and heap[0] <= start:
                popped = heapq.heappop(heap)
                # print("popped: ", popped)
            
            heapq.heappush(heap, end)
            ret = max(ret, len(heap))

            # print(interval, " : ", ret)
        return ret

        