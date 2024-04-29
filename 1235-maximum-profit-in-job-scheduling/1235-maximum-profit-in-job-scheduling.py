class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = []
        N = len(startTime)
        for i in range(N):
            jobs.append([startTime[i], endTime[i], profit[i]])
        
        jobs.sort(key=lambda x:x[0])
                
        cache = {}
        
        def dp(cur):
            print(cur)
            if cur in cache:
                return cache[cur]
            
            if cur == len(jobs):
                return 0
            
            nextIndex = bisect.bisect_left(jobs, jobs[cur][1], key=lambda x:x[0])            
            cache[cur] = max(dp(nextIndex) + jobs[cur][2], dp(cur+1))
            
            return cache[cur]
        
        maxprofix = dp(0)
        # print(cache)
        # # print(cache)
        return maxprofix
        
        