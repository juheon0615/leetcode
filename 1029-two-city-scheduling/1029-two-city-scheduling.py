class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        
        ret = 0
        a = b = len(costs) // 2
        
        
        for cost in costs:
            if a == 0:
                ret += cost[1]
            elif b == 0:
                ret += cost[0]
            else:
                if cost[0] > cost[1]:
                    ret += cost[1]
                    b -= 1
                elif cost[0] < cost[1]:
                    ret += cost[0]
                    a -= 1
                else:
                    ret += cost[0]
    
        return ret
        