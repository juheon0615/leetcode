class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: # 17
        
        total_sum = 0
        cur_sum = 0
        ans = 0
        for i in range(len(gas)):
            total_sum += gas[i] - cost[i]
            cur_sum += gas[i] - cost[i]
            
            if cur_sum < 0:
                cur_sum = 0 
                ans = i + 1
        
        # print(total_sum)
        return ans if total_sum >= 0 else -1
        
            
        