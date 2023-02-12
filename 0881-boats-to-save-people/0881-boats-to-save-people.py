class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ret = 0
        
        people.sort()
        people.reverse()
        cnts = {}
        
        for p in people:
            if p not in cnts:
                cnts[p] = 0            
            cnts[p] += 1

        for p in people:
            if cnts[p] == 0:
                continue
                
            cnts[p] -= 1
                
            r = limit - p
            
            if r == 0:
                ret += 1
                continue
            
            paired = False
            while r > 0:
                if r in cnts and cnts[r] > 0:
                    cnts[r] -= 1
                    ret += 1
                    paired = True
                    break
                else:
                    r -= 1
            
            if not paired:
                ret += 1
        
            
        return ret
        
        