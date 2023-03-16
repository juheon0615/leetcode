class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums = {}
        ret = 0

        for p in people:
            if p not in nums:
                nums[p] = 0
            nums[p] += 1
        
        
        people.sort(reverse=True)
        
        
        for p in people:
            if nums[p] == 0:
                continue
            
            nums[p] -= 1
            
            diff = limit - p
            
            while diff > 0:
                if diff in nums and nums[diff] > 0:
                    nums[diff] -= 1
                    break
                else:
                    diff -= 1
            
            ret += 1
        
        return ret
            
    
        
        
        
        