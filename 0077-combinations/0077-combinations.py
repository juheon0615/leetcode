class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(prev, counter, comb, ret):
            if len(comb) == k:
                ret.append(comb[:])
                return
            
            for i in counter:
                if i > prev and counter[i] > 0:
                    comb.append(i)
                    counter[i] = 0
                    backtrack(i, counter, comb, ret)
                    comb.pop(-1)
                    counter[i] = 1
        
        counter = Counter([i+1 for i in range(n)])
        
        ret = []
        
        backtrack(-1, counter, [], ret)
        return ret
        