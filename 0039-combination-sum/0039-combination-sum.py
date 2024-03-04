class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        
        def bt(cur, sums, ii):
            if sums == target:
                result.append(list(cur))
                return
            elif sums > target:
                return
            
            for i in range(ii, len(candidates)):
                cur.append(candidates[i])
                
                bt(cur, sums + candidates[i], i)
                
                cur.pop()
        
        bt([], 0, 0)
        
        return result
        
        
        
        