class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ret = 0
        left = 0
        cnts = {}
        left = 0
        
        for i, fruit in enumerate(fruits):
            
            if fruit not in cnts:
                cnts[fruit] = 0
            
            cnts[fruit] += 1
            # print(cnts)
            
            while len(cnts) > 2:
                f = fruits[left]
                cnts[f] -= 1
                if cnts[f] == 0:
                    del cnts[f]
                left += 1
            
            ret = max(ret, i - left + 1)
            
                
            
        
        return ret
        
        