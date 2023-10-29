class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        at step i min cost is min(step[i-1],step[i-2]) + step[i]
        '''
        
        
        
        n = len(cost)
        steps = [0 for _ in range(n+1)]
        steps[0] = cost[0]
        steps[1] = cost[1]
        
        
        for i in range(2, n+1):
            if i == n:
                steps[i] = min(steps[i-1], steps[i-2])
            else:
                steps[i] = min(steps[i-1], steps[i-2]) + cost[i]
        
        
        return steps[n]